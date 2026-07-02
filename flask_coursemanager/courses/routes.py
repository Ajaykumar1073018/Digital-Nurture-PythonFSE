from flask import Blueprint, jsonify, request
from .models import db, Course, Student, Enrollment

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

def make_response_json(data, status_code=200):
    return jsonify({'status': 'success', 'data': data}), status_code

@courses_bp.route('/', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    # Serialize the list of course objects to dictionaries
    return make_response_json([c.to_dict() for c in courses])

@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()
    
    if not data or not all(k in data for k in ('name', 'code', 'credits')):
        return jsonify({'error': 'Missing required fields: name, code, credits'}), 400
    
    new_course = Course(
        name=data['name'], 
        code=data['code'], 
        credits=data['credits'],
        department_id=data.get('department_id')
    )
    
    db.session.add(new_course)
    db.session.commit()
    
    return make_response_json(new_course.to_dict(), 201)

@courses_bp.route('/<int:course_id>/', methods=['GET'])
def get_course(course_id):
    # This automatically returns 404 if the course ID doesn't exist
    course = Course.query.get_or_404(course_id)
    return make_response_json(course.to_dict())

@courses_bp.route('/<int:course_id>/', methods=['PUT'])
def update_course(course_id):
    course = Course.query.get_or_404(course_id)
    data = request.get_json()
    
    course.name = data.get('name', course.name)
    course.code = data.get('code', course.code)
    course.credits = data.get('credits', course.credits)
    course.department_id = data.get('department_id', course.department_id)
    
    db.session.commit()
    return make_response_json(course.to_dict())

@courses_bp.route('/<int:course_id>/', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return '', 204

@courses_bp.route('/<int:course_id>/students/', methods=['GET'])
def get_enrolled_students(course_id):
    course = Course.query.get_or_404(course_id)
    # Using the relationship defined in the model to fetch students
    students = [enrollment.student.to_dict() for enrollment in course.enrollments]
    return make_response_json(students)