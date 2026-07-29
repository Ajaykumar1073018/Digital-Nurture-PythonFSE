import { useParams, useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { enroll } from './enrollmentSlice';

export default function CourseDetailPage() {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch();

  // Mocking course data for demonstration
  const course = { id: courseId, name: `Course ${courseId}`, code: `CS10${courseId}`, credits: 4 };

  const handleEnroll = () => {
    dispatch(enroll(course));
    navigate('/profile'); // Redirect to profile
  };

  return (
    <div>
      <h2>{course.name} Details</h2>
      <p>Course Code: {course.code}</p>
      <button onClick={handleEnroll}>Enroll Now</button>
    </div>
  );
}