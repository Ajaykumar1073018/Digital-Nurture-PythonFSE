from fastapi import FastAPI, Depends, HTTPException, status, Request, Response
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from typing import Optional
from contextlib import asynccontextmanager
from jose import jwt, JWTError
import httpx

import models, schemas, security
from database import engine, get_db, Base

# --- LIFESPAN & APP SETUP ---

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="Course Management API v1",
    description="A robust API with JWT Authentication and Microservices.",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom Error Handler (Hands-On 8)
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    error_code = "NOT_FOUND" if exc.status_code == 404 else "ERROR"
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": {"code": error_code, "message": exc.detail, "field": None}}
    )

# --- AUTHENTICATION & SECURITY (Hands-On 9) ---

# This exact line triggers the green "Authorize" button in Swagger UI
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login/")

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, security.SECRET_KEY, algorithms=[security.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    result = await db.execute(select(models.User).filter(models.User.email == email))
    user = result.scalar_one_or_none()
    if user is None:
        raise credentials_exception
    return user

@app.post("/api/v1/auth/register/", status_code=status.HTTP_201_CREATED, tags=['Auth'])
async def register(user_data: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.User).filter(models.User.email == user_data.email))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Email already registered")
        
    hashed_pw = security.get_password_hash(user_data.password)
    new_user = models.User(email=user_data.email, hashed_password=hashed_pw)
    db.add(new_user)
    await db.commit()
    return {"message": "User registered successfully"}

@app.post("/api/v1/auth/login/", tags=['Auth'])
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.User).filter(models.User.email == form_data.username))
    user = result.scalar_one_or_none()
    
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
        
    access_token = security.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# --- PROTECTED COURSES ENDPOINTS ---

@app.post('/api/v1/courses/', response_model=schemas.CourseResponse, status_code=status.HTTP_201_CREATED, tags=['Courses v1'])
async def create_course(
    course: schemas.CourseCreate, 
    response: Response, 
    db: AsyncSession = Depends(get_db),
    # IMPORTANT: This parameter is what puts the lock icon next to the route in Swagger!
    current_user: models.User = Depends(get_current_user) 
):
    db_course = models.Course(**course.model_dump())
    db.add(db_course)
    await db.commit()
    await db.refresh(db_course)
    response.headers['Location'] = f"/api/v1/courses/{db_course.id}"
    return db_course

@app.get('/api/v1/courses/', response_model=schemas.PaginatedCourseResponse, tags=['Courses v1'])
async def get_courses(request: Request, page: int = 1, page_size: int = 10, search: Optional[str] = None, db: AsyncSession = Depends(get_db)):
    skip = (page - 1) * page_size
    query = select(models.Course)
    if search:
        query = query.filter(models.Course.name.ilike(f"%{search}%") | models.Course.code.ilike(f"%{search}%"))
        
    total = await db.scalar(select(func.count()).select_from(query.subquery()))
    result = await db.execute(query.offset(skip).limit(page_size))
    courses = result.scalars().all()
    
    base_url = str(request.url).split('?')[0]
    return {
        "count": total,
        "next": f"{base_url}?page={page+1}&page_size={page_size}" if (page * page_size) < total else None,
        "previous": f"{base_url}?page={page-1}&page_size={page_size}" if page > 1 else None,
        "results": courses
    }

@app.delete('/api/v1/courses/{course_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Courses v1'])
async def delete_course(
    course_id: int, 
    db: AsyncSession = Depends(get_db), 
    current_user: models.User = Depends(get_current_user) # Protected!
):
    result = await db.execute(select(models.Course).filter(models.Course.id == course_id))
    course = result.scalar_one_or_none()
    if course is None:
        raise HTTPException(status_code=404, detail=f'Course with id {course_id} does not exist')
    await db.delete(course)
    await db.commit()
    return None

# --- MICROSERVICE COMMUNICATION (Hands-On 10) ---

@app.post('/api/v1/enrollments/', response_model=schemas.EnrollmentResponse, status_code=status.HTTP_201_CREATED, tags=['Enrollments v1'])
async def create_enrollment(
    enrollment: schemas.EnrollmentCreate, 
    response: Response, 
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user) # Protected!
):
    # 1. Save the enrollment to the database
    db_enrollment = models.Enrollment(**enrollment.model_dump())
    db.add(db_enrollment)
    await db.commit()
    await db.refresh(db_enrollment)
    
    response.headers['Location'] = f"/api/v1/enrollments/{db_enrollment.id}"
    
    # 2. Call the Notification Microservice running on Port 8001
    student_email = f"student_{enrollment.student_id}@college.edu"
    notification_payload = {
        "student_email": student_email,
        "course_id": enrollment.course_id
    }
    
    try:
        async with httpx.AsyncClient() as client:
            await client.post("http://127.0.0.1:8001/api/v1/notify/", json=notification_payload)
    except httpx.RequestError as exc:
        print(f"Failed to reach notification service: {exc}")
    
    return db_enrollment