const courses = [
  { id: 1, name: "Introduction to Programming", code: "CS101", credits: 3 },
  { id: 2, name: "Web Development Fundamentals", code: "CS201", credits: 4 },
  { id: 3, name: "Data Structures & Algorithms", code: "CS301", credits: 4 },
  { id: 4, name: "Database Management", code: "CS401", credits: 3 },
  { id: 5, name: "Cloud Computing Basics", code: "CS501", credits: 3 }
];

const grid = document.querySelector('.course-grid');
const searchInput = document.getElementById('search-courses');
const resultsCount = document.getElementById('search-results-count');
const totalCreditsEl = document.getElementById('total-credits');

function renderCourses(courseArray) {
  grid.innerHTML = '';
  let totalCredits = 0;

  courseArray.forEach(course => {
    const article = document.createElement('article');
    article.className = 'course-card';
    
    // Accessibility: Makes the card focusable via the Tab key
    article.setAttribute('tabindex', '0');
    
    article.innerHTML = `
      <h3>${course.name}</h3>
      <p>Code: <strong>${course.code}</strong></p>
      <span>Credits: ${course.credits}</span>
    `;
    grid.appendChild(article);
    totalCredits += course.credits;
  });

  // Accessibility: Update the aria-live region for screen readers
  resultsCount.textContent = `${courseArray.length} courses found.`;
  totalCreditsEl.textContent = `Total Credits: ${totalCredits}`;
}

// Filter courses when typing
searchInput.addEventListener('input', (e) => {
  const term = e.target.value.toLowerCase();
  const filtered = courses.filter(c => c.name.toLowerCase().includes(term));
  renderCourses(filtered);
});

// Click interaction
grid.addEventListener('click', (e) => {
  const card = e.target.closest('.course-card');
  if (card) alert('Course selected: ' + card.querySelector('h3').textContent);
});

// Accessibility: Keyboard interaction (Enter key)
grid.addEventListener('keydown', (e) => {
  const card = e.target.closest('.course-card');
  if (e.key === 'Enter' && card) {
    alert('Course selected via keyboard: ' + card.querySelector('h3').textContent);
  }
});

// Initial Render
renderCourses(courses);