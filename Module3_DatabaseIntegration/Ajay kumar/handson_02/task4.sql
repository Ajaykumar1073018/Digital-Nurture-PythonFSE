-- ===========================
-- Hands-On 2 : Task 4
-- Aggregations and Grouping
-- ===========================

-- 30. Total enrollments per course
SELECT
    c.course_name,
    COUNT(e.enrollment_id) AS enrollment_count
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;

-- 31. Average salary of professors per department
SELECT
    d.dept_name,
    ROUND(AVG(p.salary), 2) AS average_salary
FROM departments d
LEFT JOIN professors p
ON d.department_id = p.department_id
GROUP BY d.department_id, d.dept_name;

-- 32. Departments where budget exceeds 600000
SELECT
    dept_name,
    budget
FROM departments
WHERE budget > 600000;

-- 33. Grade distribution for course CS101
SELECT
    e.grade,
    COUNT(*) AS grade_count
FROM enrollments e
JOIN courses c
ON e.course_id = c.course_id
WHERE c.course_code = 'CS101'
GROUP BY e.grade;

-- 34. Departments with more than 2 enrolled students
SELECT
    d.dept_name,
    COUNT(e.student_id) AS total_students
FROM departments d
JOIN students s
ON d.department_id = s.department_id
JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY d.department_id, d.dept_name
HAVING COUNT(e.student_id) > 2;
