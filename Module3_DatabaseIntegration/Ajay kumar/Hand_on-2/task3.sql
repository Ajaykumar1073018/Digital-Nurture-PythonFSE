-- ===========================
-- Hands-On 2 : Task 3
-- Multi-Table Joins
-- ===========================

-- 25. Student full name with department name
SELECT
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    d.dept_name
FROM students s
JOIN departments d
ON s.department_id = d.department_id;

-- 26. Enrollment with student name and course name
SELECT
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    c.course_name,
    e.enrollment_date,
    e.grade
FROM enrollments e
JOIN students s
ON e.student_id = s.student_id
JOIN courses c
ON e.course_id = c.course_id;

-- 27. Students not enrolled in any course
SELECT
    s.student_id,
    s.first_name,
    s.last_name
FROM students s
LEFT JOIN enrollments e
ON s.student_id = e.student_id
WHERE e.student_id IS NULL;

-- 28. Every course with number of enrolled students
SELECT
    c.course_name,
    COUNT(e.student_id) AS enrollment_count
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;

-- 29. Departments with professors and salaries
SELECT
    d.dept_name,
    p.prof_name,
    p.salary
FROM departments d
LEFT JOIN professors p
ON d.department_id = p.department_id;
