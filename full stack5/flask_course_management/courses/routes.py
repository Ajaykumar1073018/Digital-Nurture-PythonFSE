from flask import Blueprint, jsonify, request
from .models import db, Course, Student

course_bp = Blueprint(
    "course_bp",
    __name__,
    url_prefix="/api/courses"
)

# GET ALL COURSES
@course_bp.route("/", methods=["GET"])
def get_courses():
    courses = Course.query.all()

    return jsonify(
        [course.to_dict() for course in courses]
    )


# GET ONE COURSE
@course_bp.route("/<int:id>/", methods=["GET"])
def get_course(id):
    course = Course.query.get_or_404(id)

    return jsonify(course.to_dict())


# CREATE COURSE
@course_bp.route("/", methods=["POST"])
def create_course():
    data = request.get_json()

    course = Course(
        title=data["title"],
        department_id=data["department_id"]
    )

    db.session.add(course)
    db.session.commit()

    return jsonify(course.to_dict()), 201


# UPDATE COURSE
@course_bp.route("/<int:id>/", methods=["PUT"])
def update_course(id):
    course = Course.query.get_or_404(id)

    data = request.get_json()

    course.title = data["title"]

    db.session.commit()

    return jsonify(course.to_dict())


# DELETE COURSE
@course_bp.route("/<int:id>/", methods=["DELETE"])
def delete_course(id):
    course = Course.query.get_or_404(id)

    db.session.delete(course)
    db.session.commit()

    return jsonify({
        "message": "Course deleted"
    })


# GET STUDENTS IN COURSE
@course_bp.route("/<int:id>/students/", methods=["GET"])
def course_students(id):

    course = Course.query.get_or_404(id)

    students = Student.query.join(
        Student.enrollments
    ).filter_by(
        course_id=id
    ).all()

    return jsonify([
        student.to_dict()
        for student in students
    ])