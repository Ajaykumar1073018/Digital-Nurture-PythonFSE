// src/App.jsx
import { Routes, Route, useNavigate, useParams } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { enroll, unenroll } from './store/enrollmentSlice';
import Header from './components/Header';
import Footer from './components/Footer';
import { initialCourses } from './data'; // Re-using our local data for speed

// --- PAGE COMPONENTS ---

const HomePage = () => (
    <div style={{ textAlign: 'center', padding: '40px' }}>
        <h1>Welcome to the Student Portal</h1>
        <p>Use the navigation bar to browse courses or view your profile.</p>
    </div>
);

const CoursesPage = () => {
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const handleEnroll = (course) => {
        dispatch(enroll(course)); // Dispatch Redux action
        navigate('/profile');     // Redirect to profile page after enrolling
    };

    return (
        <div>
            <h2>Available Courses</h2>
            {initialCourses.map(course => (
                <div key={course.id} style={{ border: '1px solid #ccc', padding: '15px', margin: '10px 0' }}>
                    <h3>{course.name}</h3>
                    <p>Code: {course.code}</p>
                    <button 
                        onClick={() => handleEnroll(course)}
                        style={{ padding: '8px 16px', backgroundColor: '#27ae60', color: 'white', cursor: 'pointer' }}
                    >
                        Enroll
                    </button>
                    {/* Link to dynamic detail page */}
                    <button 
                        onClick={() => navigate(`/courses/${course.id}`)}
                        style={{ marginLeft: '10px', padding: '8px 16px', cursor: 'pointer' }}
                    >
                        View Details
                    </button>
                </div>
            ))}
        </div>
    );
};

const CourseDetailPage = () => {
    const { courseId } = useParams(); // Extract URL parameter
    const course = initialCourses.find(c => c.id === parseInt(courseId));

    if (!course) return <h2>Course not found!</h2>;

    return (
        <div>
            <h2>Course Details for: {course.code}</h2>
            <h3>{course.name}</h3>
            <p>Credits: {course.credits}</p>
            <p>Grade: {course.grade}</p>
        </div>
    );
};

const ProfilePage = () => {
    const dispatch = useDispatch();
    const enrolledCourses = useSelector(state => state.enrollment.enrolledCourses);

    return (
        <div>
            <h2>Your Profile & Enrollments</h2>
            {enrolledCourses.length === 0 ? <p>You are not enrolled in any courses.</p> : null}
            
            {enrolledCourses.map(course => (
                <div key={course.id} style={{ border: '1px solid #3498db', padding: '10px', margin: '10px 0' }}>
                    <strong>{course.name}</strong> 
                    <button 
                        onClick={() => dispatch(unenroll(course.id))}
                        style={{ float: 'right', backgroundColor: '#e74c3c', color: 'white', border: 'none', padding: '5px 10px', cursor: 'pointer' }}
                    >
                        Remove
                    </button>
                </div>
            ))}
        </div>
    );
};


// --- MAIN APP COMPONENT ---

export default function App() {
    return (
        <div style={{ fontFamily: 'Arial, sans-serif' }}>
            <Header siteName="Student Portal (Redux + Router)" />
            
            <main style={{ padding: '20px', maxWidth: '800px', margin: '0 auto', minHeight: '60vh' }}>
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/courses" element={<CoursesPage />} />
                    <Route path="/courses/:courseId" element={<CourseDetailPage />} />
                    <Route path="/profile" element={<ProfilePage />} />
                </Routes>
            </main>

            <Footer />
        </div>
    );
}