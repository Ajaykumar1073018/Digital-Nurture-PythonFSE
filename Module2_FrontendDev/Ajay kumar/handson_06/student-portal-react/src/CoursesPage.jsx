import { useState, useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { enroll } from './enrollmentSlice';
import CourseCard from './components/CourseCard';

export default function CoursesPage() {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const dispatch = useDispatch();

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/posts?_limit=5')
      .then(res => res.json())
      .then(data => {
        const mappedData = data.map(post => ({
          id: post.id, name: post.title, code: `CS10${post.id}`, credits: 4, grade: 'A'
        }));
        setCourses(mappedData);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading courses...</p>;

  return (
    <div className="course-grid">
      {courses.map(course => (
        <CourseCard 
          key={course.id} 
          {...course} 
          onEnroll={() => dispatch(enroll(course))} 
        />
      ))}
    </div>
  );
}