"""
===========================================================
Hands-On 6
Task 2 : CRUD Operations using SQLAlchemy
Task 3 : Solving N+1 Problem using joinedload()

N+1 Problem

Without joinedload():
---------------------
1 query fetches enrollments
Then 1 query per student
Then 1 query per course

Total Queries ≈ 13

With joinedload():
------------------
Only ONE SQL query is executed using JOIN.

This improves application performance significantly.
===========================================================
"""

from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload

from models import (
    Base,
    Department,
    Student,
    Course,
    Enrollment,
    Professor
)

# -------------------------------------------------
# Database Connection
# -------------------------------------------------

DATABASE_URL = "postgresql://postgres:password@localhost/college_db_orm"

# For MySQL use:
# DATABASE_URL = "mysql+mysqlconnector://root:password@localhost/college_db_orm"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# =====================================================
# TASK 2
# CRUD OPERATIONS
# =====================================================

print("\n========== INSERT DEPARTMENTS ==========\n")

dept1 = Department(
    dept_name="Computer Science",
    hod_name="Dr. Ramesh Kumar",
    budget=850000
)

dept2 = Department(
    dept_name="Electronics",
    hod_name="Dr. Priya Nair",
    budget=620000
)

dept3 = Department(
    dept_name="Mechanical",
    hod_name="Dr. Suresh Iyer",
    budget=540000
)

session.add_all([dept1, dept2, dept3])
session.commit()

print("Departments Inserted Successfully")


# =====================================================

print("\n========== INSERT STUDENTS ==========\n")

student1 = Student(
    first_name="Arjun",
    last_name="Mehta",
    email="arjun@gmail.com",
    date_of_birth=date(2003,4,12),
    department=dept1,
    enrollment_year=2022
)

student2 = Student(
    first_name="Priya",
    last_name="Suresh",
    email="priya@gmail.com",
    date_of_birth=date(2003,7,25),
    department=dept1,
    enrollment_year=2022
)

student3 = Student(
    first_name="Rohan",
    last_name="Verma",
    email="rohan@gmail.com",
    date_of_birth=date(2002,11,8),
    department=dept2,
    enrollment_year=2021
)

student4 = Student(
    first_name="Sneha",
    last_name="Patel",
    email="sneha@gmail.com",
    date_of_birth=date(2004,1,30),
    department=dept3,
    enrollment_year=2023
)

student5 = Student(
    first_name="Vikram",
    last_name="Das",
    email="vikram@gmail.com",
    date_of_birth=date(2003,9,14),
    department=dept1,
    enrollment_year=2022
)

session.add_all([
    student1,
    student2,
    student3,
    student4,
    student5
])

session.commit()

print("Students Inserted Successfully")


# =====================================================

print("\n========== INSERT COURSES ==========\n")

course1 = Course(
    course_name="Database Management Systems",
    course_code="CS102",
    credits=3,
    department=dept1
)

course2 = Course(
    course_name="Object Oriented Programming",
    course_code="CS103",
    credits=4,
    department=dept1
)

course3 = Course(
    course_name="Circuit Theory",
    course_code="EC101",
    credits=3,
    department=dept2
)

session.add_all([
    course1,
    course2,
    course3
])

session.commit()

print("Courses Inserted Successfully")


# =====================================================

print("\n========== INSERT ENROLLMENTS ==========\n")

enrollment1 = Enrollment(
    student=student1,
    course=course1,
    enrollment_date=date.today(),
    grade="A"
)

enrollment2 = Enrollment(
    student=student2,
    course=course1,
    enrollment_date=date.today(),
    grade="B"
)

enrollment3 = Enrollment(
    student=student3,
    course=course3,
    enrollment_date=date.today(),
    grade="A"
)

enrollment4 = Enrollment(
    student=student5,
    course=course2,
    enrollment_date=date.today(),
    grade="A"
)

session.add_all([
    enrollment1,
    enrollment2,
    enrollment3,
    enrollment4
])

session.commit()

print("Enrollments Inserted Successfully")


# =====================================================
# READ
# =====================================================

print("\n========== COMPUTER SCIENCE STUDENTS ==========\n")

students = (
    session.query(Student)
    .join(Department)
    .filter(
        Department.dept_name == "Computer Science"
    )
    .all()
)

for student in students:
    print(
        student.first_name,
        student.last_name,
        student.email
    )


# =====================================================
# READ ENROLLMENTS
# =====================================================

print("\n========== ENROLLMENTS ==========\n")

enrollments = session.query(Enrollment).all()

for enrollment in enrollments:

    print(
        enrollment.student.first_name,
        "->",
        enrollment.course.course_name,
        "-",
        enrollment.grade
    )


# =====================================================
# UPDATE
# =====================================================

print("\n========== UPDATE ==========\n")

student = (
    session.query(Student)
    .filter_by(email="vikram@gmail.com")
    .first()
)

if student:

    student.enrollment_year = 2024

    session.commit()

    print("Student Updated Successfully")


# =====================================================
# DELETE
# =====================================================

print("\n========== DELETE ==========\n")

delete_record = (
    session.query(Enrollment)
    .first()
)

if delete_record:

    session.delete(delete_record)

    session.commit()

    print("Enrollment Deleted Successfully")
