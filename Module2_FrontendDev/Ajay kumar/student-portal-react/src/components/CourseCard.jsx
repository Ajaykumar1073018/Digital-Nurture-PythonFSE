// src/components/CourseCard.jsx
export default function CourseCard({ course, onEnroll }) {
    return (
        <article style={{ border: '1px solid #ccc', padding: '15px', margin: '10px 0', borderRadius: '5px' }}>
            <h3 style={{ color: '#2980b9', margin: '0 0 10px 0' }}>{course.name}</h3>
            <p>Code: <strong>{course.code}</strong> | Credits: {course.credits}</p>
            <button 
                onClick={() => onEnroll(course)}
                style={{ padding: '8px 16px', backgroundColor: '#27ae60', color: 'white', border: 'none', cursor: 'pointer' }}
            >
                Enroll
            </button>
        </article>
    );
}