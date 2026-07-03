from pydantic import BaseModel, EmailStr


class CourseCreate(BaseModel):
    title: str
    instructor: str


class CourseResponse(CourseCreate):
    id: int

    class Config:
        from_attributes = True


class StudentCreate(BaseModel):
    name: str
    email: EmailStr


class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True


class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int


class EnrollmentResponse(EnrollmentCreate):
    id: int

    class Config:
        from_attributes = True