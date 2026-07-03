from fastapi import FastAPI, HTTPException, Response, Query, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="REST API Best Practices")

# -----------------------------
# URL Versioning:
# /api/v1/courses/
#
# Alternative:
# Header Versioning:
# Accept: application/vnd.api+json;version=1
# -----------------------------

courses = [
    {
        "id": 1,
        "name": "Python",
        "code": "PY101",
        "instructor": "John"
    },
    {
        "id": 2,
        "name": "FastAPI",
        "code": "FA102",
        "instructor": "David"
    },
    {
        "id": 3,
        "name": "Machine Learning",
        "code": "ML103",
        "instructor": "Alice"
    }
]


class CourseCreate(BaseModel):
    name: str
    code: str
    instructor: str


class CourseUpdate(BaseModel):
    name: str
    code: str
    instructor: str


class CoursePatch(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    instructor: Optional[str] = None


def error_response(code, message, field=None):
    return {
        "error": {
            "code": code,
            "message": message,
            "field": field
        }
    }


# GET ALL COURSES WITH PAGINATION AND SEARCH
@app.get("/api/v1/courses/")
def get_courses(
    page: int = Query(1, ge=1),
    page_size: int = Query(2, ge=1),
    search: Optional[str] = None
):

    filtered = courses

    if search:
        search = search.lower()
        filtered = [
            c for c in courses
            if search in c["name"].lower()
            or search in c["code"].lower()
        ]

    total = len(filtered)

    start = (page - 1) * page_size
    end = start + page_size

    results = filtered[start:end]

    next_page = None
    previous_page = None

    if end < total:
        next_page = (
            f"/api/v1/courses/?page={page+1}"
            f"&page_size={page_size}"
        )

    if page > 1:
        previous_page = (
            f"/api/v1/courses/?page={page-1}"
            f"&page_size={page_size}"
        )

    return {
        "count": total,
        "next": next_page,
        "previous": previous_page,
        "results": results
    }


# GET COURSE BY ID
@app.get("/api/v1/courses/{course_id}")
def get_course(course_id: int):

    for course in courses:
        if course["id"] == course_id:
            return course

    raise HTTPException(
        status_code=404,
        detail=error_response(
            "NOT_FOUND",
            f"Course with id {course_id} does not exist"
        )
    )


# CREATE COURSE
@app.post("/api/v1/courses/", status_code=201)
def create_course(course: CourseCreate, response: Response):

    new_id = max(c["id"] for c in courses) + 1

    new_course = {
        "id": new_id,
        "name": course.name,
        "code": course.code,
        "instructor": course.instructor
    }

    courses.append(new_course)

    response.headers["Location"] = (
        f"/api/v1/courses/{new_id}"
    )

    return new_course


# PUT - FULL UPDATE
@app.put("/api/v1/courses/{course_id}")
def update_course(course_id: int, updated: CourseUpdate):

    for course in courses:

        if course["id"] == course_id:
            course["name"] = updated.name
            course["code"] = updated.code
            course["instructor"] = updated.instructor
            return course

    raise HTTPException(
        status_code=404,
        detail=error_response(
            "NOT_FOUND",
            f"Course with id {course_id} does not exist"
        )
    )


# PATCH - PARTIAL UPDATE
@app.patch("/api/v1/courses/{course_id}")
def patch_course(course_id: int, updated: CoursePatch):

    for course in courses:

        if course["id"] == course_id:

            if updated.name is not None:
                course["name"] = updated.name

            if updated.code is not None:
                course["code"] = updated.code

            if updated.instructor is not None:
                course["instructor"] = updated.instructor

            return course

    raise HTTPException(
        status_code=404,
        detail=error_response(
            "NOT_FOUND",
            f"Course with id {course_id} does not exist"
        )
    )


# DELETE COURSE
@app.delete(
    "/api/v1/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_course(course_id: int):

    for course in courses:

        if course["id"] == course_id:
            courses.remove(course)
            return Response(status_code=204)

    raise HTTPException(
        status_code=404,
        detail=error_response(
            "NOT_FOUND",
            f"Course with id {course_id} does not exist"
        )
    )