export default function CourseCard({ name, code, credits, grade, onEnroll }) {
  return (
    <article className="course-card">
      <h3>{name}</h3>
      <p>Code: {code}</p>
      <span>Credits: {credits}</span>
      {grade && <p>Grade: {grade}</p>}
      <button onClick={onEnroll}>Enroll</button>
    </article>
  );
}