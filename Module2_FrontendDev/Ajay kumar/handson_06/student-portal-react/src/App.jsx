import { Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import HomePage from './HomePage';
import CoursesPage from './CoursesPage';
import ProfilePage from './ProfilePage';
import CourseDetailPage from './CourseDetailPage';

export default function App() {
  return (
    <>
      <Header siteName="Student Portal" />
      <main>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/courses" element={<CoursesPage />} />
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="/courses/:courseId" element={<CourseDetailPage />} />
        </Routes>
      </main>
      <Footer />
    </>
  );
}