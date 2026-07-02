from pydantic import BaseModel
from typing import Optional, List, Any

# --- COURSE & DEPARTMENT SCHEMAS (Hands-On 6) ---

class CourseBase(BaseModel):
    name: str
    code: str
    credits: int
    department_id: Optional[int] = None

class CourseCreate(CourseBase):
    pass

class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None

class CourseResponse(CourseBase):
    id: int
    
    class Config:
        from_attributes = True

class DepartmentResponse(BaseModel):
    id: int
    name: str
    courses: List[CourseResponse] = []
    
    class Config:
        from_attributes = True


# --- STUDENT & ENROLLMENT SCHEMAS (Hands-On 7) ---

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    department_id: int
    enrollment_year: int

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    class Config:
        from_attributes = True

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

class EnrollmentResponse(EnrollmentCreate):
    id: int
    grade: Optional[str] = None
    class Config:
        from_attributes = True


# --- PAGINATION SCHEMA (Hands-On 8) ---

class PaginatedCourseResponse(BaseModel):
    count: int
    next: Optional[str] = None
    previous: Optional[str] = None
    results: List[CourseResponse]


# --- USER AUTH SCHEMAS (Hands-On 9) ---

class UserCreate(BaseModel):
    email: str
    password: str