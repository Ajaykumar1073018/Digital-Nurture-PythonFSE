from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from models import Course, Student, Enrollment
from schemas import (
    CourseCreate,
    CourseResponse,
    StudentCreate,
    StudentResponse,
    EnrollmentCreate,
    EnrollmentResponse
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Course Management API",
    description="FastAPI CRUD API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Course Management API is running"}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def send_confirmation_email(email):
    print(f"Sending confirmation to {email}")


# ---------------- COURSES ----------------

@app.post(
    "/api/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"]
)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    new_course = Course(
        title=course.title,
        instructor=course.instructor
    )

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course


@app.get(
    "/api/courses/",
    response_model=list[CourseResponse],
    tags=["Courses"]
)
def get_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()


@app.get(
    "/api/courses/{id}",
    response_model=CourseResponse,
    tags=["Courses"]
)
def get_course(id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == id).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


@app.put(
    "/api/courses/{id}",
    response_model=CourseResponse,
    tags=["Courses"]
)
def update_course(
    id: int,
    course_data: CourseCreate,
    db: Session = Depends(get_db)
):
    course = db.query(Course).filter(Course.id == id).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    course.title = course_data.title
    course.instructor = course_data.instructor

    db.commit()
    db.refresh(course)

    return course


@app.delete(
    "/api/courses/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Courses"]
)
def delete_course(id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == id).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    db.delete(course)
    db.commit()


@app.get(
    "/api/courses/{id}/students/",
    tags=["Courses"]
)
def get_course_students(id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == id).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    students = (
        db.query(Student)
        .join(Enrollment)
        .filter(Enrollment.course_id == id)
        .all()
    )

    return students


# ---------------- STUDENTS ----------------

@app.post(
    "/api/students/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Students"]
)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(
        name=student.name,
        email=student.email
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


@app.get(
    "/api/students/",
    response_model=list[StudentResponse],
    tags=["Students"]
)
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()


@app.get(
    "/api/students/{id}",
    response_model=StudentResponse,
    tags=["Students"]
)
def get_student(id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == id).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@app.put(
    "/api/students/{id}",
    response_model=StudentResponse,
    tags=["Students"]
)
def update_student(
    id: int,
    student_data: StudentCreate,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.id == id).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.name = student_data.name
    student.email = student_data.email

    db.commit()
    db.refresh(student)

    return student


@app.delete(
    "/api/students/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Students"]
)
def delete_student(id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == id).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()


# ---------------- ENROLLMENTS ----------------

@app.post(
    "/api/enrollments/",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Enrollments"]
)
def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.id == enrollment.student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    new_enrollment = Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id
    )

    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)

    background_tasks.add_task(
        send_confirmation_email,
        student.email
    )

    return new_enrollment


@app.get(
    "/api/enrollments/",
    response_model=list[EnrollmentResponse],
    tags=["Enrollments"]
)
def get_enrollments(db: Session = Depends(get_db)):
    return db.query(Enrollment).all()


@app.delete(
    "/api/enrollments/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Enrollments"]
)
def delete_enrollment(id: int, db: Session = Depends(get_db)):
    enrollment = db.query(Enrollment).filter(
        Enrollment.id == id
    ).first()

    if not enrollment:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    db.delete(enrollment)
    db.commit()