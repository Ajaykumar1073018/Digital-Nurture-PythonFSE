export default function Header(props) {
  return (
    <header>
      <h1>{props.siteName}</h1>
      <nav>
        <ul style={{ display: 'flex', gap: '1rem', listStyle: 'none' }}>
          <li><a href="/">Home</a></li>
          <li><a href="/courses">Courses</a></li>
          <li><a href="/profile">Profile</a></li>
        </ul>
      </nav>
      <div>
        <strong>Enrolled: {props.enrolledCount || 0}</strong>
      </div>
    </header>
  );
}