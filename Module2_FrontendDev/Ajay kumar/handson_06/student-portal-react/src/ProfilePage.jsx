import { useSelector, useDispatch } from 'react-redux';
import { unenroll } from './enrollmentSlice';
import StudentProfile from './components/StudentProfile';

export default function ProfilePage() {
  const enrolledCourses = useSelector(state => state.enrollment.enrolledCourses);
  const dispatch = useDispatch();

  return (
    <div>
      <StudentProfile />
      <hr />
      <h3>Your Enrolled Courses</h3>
      {enrolledCourses.length === 0 ? (
        <p>You have not enrolled in any courses yet.</p>
      ) : (
        <ul>
          {enrolledCourses.map(course => (
            <li key={course.id}>
              {course.name} ({course.code}) 
              <button onClick={() => dispatch(unenroll(course.id))}>Remove</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}