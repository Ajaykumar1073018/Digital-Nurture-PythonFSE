import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';

export default function Header({ siteName }) {
  // Pulling the enrolled courses array from your Redux store
  const enrolledCourses = useSelector((state) => state.enrollment.enrolledCourses);

  return (
    <header>
      <h1>{siteName}</h1>
      <nav>
        <ul style={{ display: 'flex', gap: '1rem', listStyle: 'none' }}>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/courses">Courses</Link></li>
          <li><Link to="/profile">Profile</Link></li>
        </ul>
      </nav>
      <div>
        <strong>Enrolled: {enrolledCourses.length}</strong>
      </div>
    </header>
  );
}