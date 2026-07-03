from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))


with app.app_context():
    db.create_all()


@app.route("/api/students", methods=["POST"])
def add_student():
    data = request.json

    student = Student(
        name=data["name"],
        email=data["email"]
    )

    db.session.add(student)
    db.session.commit()

    return jsonify({
        "id": student.id,
        "name": student.name,
        "email": student.email
    })


@app.route("/api/students", methods=["GET"])
def get_students():
    students = Student.query.all()

    result = []

    for s in students:
        result.append({
            "id": s.id,
            "name": s.name,
            "email": s.email
        })

    return jsonify(result)


@app.route("/api/students/<int:id>/enroll", methods=["POST"])
def enroll(id):

    student = Student.query.get(id)

    if not student:
        return jsonify({"message": "Student not found"}), 404

    course_id = request.json["course_id"]

    try:
        response = requests.get(
            f"http://localhost:5001/api/courses/{course_id}"
        )

        if response.status_code != 200:
            return jsonify({"message": "Course not found"}), 404

    except requests.exceptions.ConnectionError:
        return jsonify({
            "message": "Course Service unavailable"
        }), 503

    return jsonify({
        "message": f"Student {id} enrolled in Course {course_id}"
    })


if __name__ == "__main__":
    app.run(port=5002, debug=True)