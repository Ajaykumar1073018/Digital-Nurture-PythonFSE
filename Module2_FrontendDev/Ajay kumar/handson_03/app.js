// 1. ES6 Import
import { coursesData } from './data.js';

// State variable to hold our current working data
let currentCourses = [...coursesData];

// ==========================================
// TASK 1: ES6+ Syntax Practice (Console Logs)
// ==========================================

// Destructuring in a loop
console.log("--- Destructuring ---");
currentCourses.forEach(course => {
    const { name, credits } = course;
    console.log(`${name} is worth ${credits} credits.`);
});

// Array.map() with template literals
const formattedCourses = currentCourses.map(course => `${course.code} ${course.name} (${course.credits} credits)`);
console.log("--- Formatted Courses (map) ---", formattedCourses);

// Array.filter()
const heavyCourses = currentCourses.filter(course => course.credits >= 4);
console.log("--- High Credit Courses Count (filter) ---", heavyCourses.length);

// Array.reduce()
const totalCredits = currentCourses.reduce((sum, course) => sum + course.credits, 0);
console.log("--- Total Credits (reduce) ---", totalCredits);


// ==========================================
// TASK 2: DOM Selection & Dynamic Rendering
// ==========================================

const courseGrid = document.querySelector('.course-grid');
const totalCreditsDisplay = document.getElementById('total-credits');

// Function to render courses to the DOM
const renderCourses = (coursesToRender) => {
    // Clear the container first to avoid duplicates
    courseGrid.innerHTML = ''; 

    // Calculate dynamic total
    const currentTotal = coursesToRender.reduce((sum, c) => sum + c.credits, 0);
    totalCreditsDisplay.textContent = `Total Enrolled Credits: ${currentTotal}`;

    // Create and append elements
    coursesToRender.forEach(course => {
        const article = document.createElement('article');
        article.className = 'course-card';
        
        // Storing data attribute for event delegation later
        article.dataset.name = course.name;
        article.dataset.grade = course.grade;

        article.innerHTML = `
            <h3>${course.name}</h3>
            <p>Course Code: <strong>${course.code}</strong></p>
            <span>Credits: ${course.credits}</span>
        `;
        
        courseGrid.appendChild(article);
    });
};

// Initial Render
renderCourses(currentCourses);


// ==========================================
// TASK 3: Event Listeners & Interactivity
// ==========================================

const searchInput = document.getElementById('search-courses');
const sortButton = document.getElementById('sort-credits');
const selectedCourseDisplay = document.getElementById('selected-course');

// Search Functionality (input event)
searchInput.addEventListener('input', (event) => {
    const searchTerm = event.target.value.toLowerCase();
    
    // Filter the original data array
    currentCourses = coursesData.filter(course => 
        course.name.toLowerCase().includes(searchTerm)
    );
    
    // Re-render with filtered data
    renderCourses(currentCourses);
});

// Sort Functionality (click event)
sortButton.addEventListener('click', () => {
    // Sort descending by credits
    currentCourses.sort((a, b) => b.credits - a.credits);
    renderCourses(currentCourses);
});

// Event Delegation (Clicking a card to see details)
courseGrid.addEventListener('click', (event) => {
    // Find the closest course-card element to the click target
    const clickedCard = event.target.closest('.course-card');
    
    if (clickedCard) {
        const courseName = clickedCard.dataset.name;
        const courseGrade = clickedCard.dataset.grade;
        
        selectedCourseDisplay.textContent = `You selected ${courseName}. Your current grade is: ${courseGrade}`;
    }
});