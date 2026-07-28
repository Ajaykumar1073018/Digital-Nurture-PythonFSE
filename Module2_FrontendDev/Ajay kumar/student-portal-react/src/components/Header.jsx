// src/components/Header.jsx
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';

export default function Header({ siteName }) {
    // Read state directly from Redux store
    const enrolledCourses = useSelector(state => state.enrollment.enrolledCourses);

    return (
        <header style={{ backgroundColor: '#2c3e50', color: 'white', padding: '20px', display: 'flex', justifyContent: 'space-between' }}>
            <h2>{siteName}</h2>
            <nav style={{ display: 'flex', gap: '15px', alignItems: 'center' }}>
                <span style={{ fontWeight: 'bold', color: '#f1c40f' }}>
                    Enrolled: {enrolledCourses.length}
                </span>
                <Link to="/" style={{ color: 'white', textDecoration: 'none' }}>Home</Link>
                <Link to="/courses" style={{ color: 'white', textDecoration: 'none' }}>Courses</Link>
                <Link to="/profile" style={{ color: 'white', textDecoration: 'none' }}>Profile</Link>
            </nav>
        </header>
    );
}