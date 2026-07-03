from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm
)

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    Session
)

from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta

# ==========================
# DATABASE
# ==========================

DATABASE_URL = "sqlite:///./auth.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# ==========================
# USER MODEL
# ==========================

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


Base.metadata.create_all(bind=engine)


# ==========================
# APP
# ==========================

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login/"
)


# ==========================
# SECURITY
# ==========================

SECRET_KEY = "mysecretkey123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# bcrypt is slow hashing.
# MD5 and SHA256 are fast and not suitable for passwords.


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=30
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


# ==========================
# DATABASE SESSION
# ==========================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==========================
# CURRENT USER
# ==========================

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid token"
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(
        User.email == email
    ).first()

    if user is None:
        raise credentials_exception

    return user


# ==========================
# HOME
# ==========================

@app.get("/")
def home():
    return {
        "message": "JWT Authentication API"
    }


# ==========================
# REGISTER
# ==========================

@app.post("/api/v1/auth/register/")
def register(
    email: str,
    password: str,
    db: Session = Depends(get_db)
):

    existing = db.query(User).filter(
        User.email == email
    ).first()

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    hashed_password = get_password_hash(
        password
    )

    user = User(
        email=email,
        hashed_password=hashed_password
    )

    db.add(user)
    db.commit()

    return {
        "message": "User registered successfully"
    }


# ==========================
# LOGIN
# ==========================

@app.post("/api/v1/auth/login/")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        form_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        {"sub": user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# ==========================
# PUBLIC ROUTE
# ==========================

@app.get("/api/v1/courses/")
def get_courses():
    return [
        {"id": 1, "name": "Python"},
        {"id": 2, "name": "FastAPI"}
    ]


# ==========================
# PROTECTED ROUTE
# ==========================

@app.post("/api/v1/courses/")
def create_course(
    current_user: User = Depends(
        get_current_user
    )
):
    return {
        "message": "Course created",
        "user": current_user.email
    }


@app.delete("/api/v1/courses/{id}")
def delete_course(
    id: int,
    current_user: User = Depends(
        get_current_user
    )
):
    return {
        "message": f"Course {id} deleted"
    }


# OAuth2 Authorization Code Flow:
# User logs in through Google/GitHub.
# Authorization server returns a code.
# Code is exchanged for a token.
#
# Simple JWT login:
# User sends username/password directly.
# Server immediately returns JWT.