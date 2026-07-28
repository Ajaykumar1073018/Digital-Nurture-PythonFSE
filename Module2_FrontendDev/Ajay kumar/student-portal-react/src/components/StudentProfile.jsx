// src/components/StudentProfile.jsx
import { useState } from 'react';

export default function StudentProfile() {
    const [profile, setProfile] = useState({ name: '', email: '', semester: '' });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setProfile(prev => ({ ...prev, [name]: value }));
    };

    return (
        <div style={{ padding: '20px', backgroundColor: '#f9f9f9', marginTop: '20px', borderRadius: '5px' }}>
            <h2>Student Profile Form</h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', maxWidth: '300px' }}>
                <input name="name" placeholder="Name" value={profile.name} onChange={handleChange} />
                <input name="email" placeholder="Email" value={profile.email} onChange={handleChange} />
                <input name="semester" placeholder="Semester" value={profile.semester} onChange={handleChange} />
            </div>
            <p style={{ marginTop: '15px' }}>
                <strong>Preview:</strong> {profile.name} | {profile.email} | Semester {profile.semester}
            </p>
        </div>
    );
}