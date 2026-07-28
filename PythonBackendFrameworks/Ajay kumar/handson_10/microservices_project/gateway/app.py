from flask import Flask, request
import requests

app = Flask(__name__)

COURSE_URL = "http://localhost:5001"
STUDENT_URL = "http://localhost:5002"


@app.route("/api/courses/", methods=["GET", "POST"])
def courses():

    response = requests.request(
        method=request.method,
        url=f"{COURSE_URL}/api/courses",
        json=request.get_json(silent=True)
    )

    return (
        response.content,
        response.status_code,
        response.headers.items()
    )


@app.route("/api/courses/<path:path>", methods=["GET"])
def course(path):

    response = requests.get(
        f"{COURSE_URL}/api/courses/{path}"
    )

    return (
        response.content,
        response.status_code,
        response.headers.items()
    )


@app.route("/api/students", methods=["GET", "POST"])
def students():

    response = requests.request(
        method=request.method,
        url=f"{STUDENT_URL}/api/students",
        json=request.get_json(silent=True)
    )

    return (
        response.content,
        response.status_code,
        response.headers.items()
    )


@app.route("/api/students/<int:id>/enroll", methods=["POST"])
def enroll(id):

    response = requests.post(
        f"{STUDENT_URL}/api/students/{id}/enroll",
        json=request.get_json()
    )

    return (
        response.content,
        response.status_code,
        response.headers.items()
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)