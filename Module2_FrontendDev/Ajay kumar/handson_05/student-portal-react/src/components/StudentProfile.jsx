import { useState } from 'react';

export default function StudentProfile() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [semester, setSemester] = useState('');

  return (
    <div className="profile-section">
      <h2>Student Profile</h2>
      <form>
        <div>
          <label>Name: </label>
          <input 
            type="text" 
            value={name} 
            onChange={(e) => setName(e.target.value)} 
          />
        </div>
        <div>
          <label>Email: </label>
          <input 
            type="email" 
            value={email} 
            onChange={(e) => setEmail(e.target.value)} 
          />
        </div>
        <div>
          <label>Semester: </label>
          <input 
            type="number" 
            value={semester} 
            onChange={(e) => setSemester(e.target.value)} 
          />
        </div>
      </form>
    </div>
  );
}