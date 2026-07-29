import { useState, useEffect } from 'react';
import Header from './components/Header';
import CourseCard from './components/CourseCard';

export default function App() {
  const [courses, setCourses] = useState([]);
  const [enrolledCourses, setEnrolledCourses] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/posts?_limit=5')
      .then(res => res.json())
      .then(data => {
        const mappedData = data.map(post => ({
          id: post.id, name: post.title, code: `CS10${post.id}`, credits: 4, grade: 'A'
        }));
        setCourses(mappedData);
        setLoading(false);
      })
      .catch(err => {
        setError('Failed to fetch courses');
        setLoading(false);
      });
  }, []);

  const handleEnroll = (course) => {
    setEnrolledCourses([...enrolledCourses, course]);
  };

  const filteredCourses = courses.filter(c => c.name.includes(searchTerm));

  return (
    <>
      <Header siteName="Student Portal" enrolledCount={enrolledCourses.length} />
      <main>
        <input 
          type="text" 
          placeholder="Search courses..." 
          onChange={(e) => setSearchTerm(e.target.value)} 
        />
        {loading && <p>Loading...</p>}
        {error && <p>{error}</p>}
        <div className="course-grid">
          {filteredCourses.map(course => (
            <CourseCard key={course.id} {...course} onEnroll={() => handleEnroll(course)} />
          ))}
        </div>
      </main>
    </>
  );
}