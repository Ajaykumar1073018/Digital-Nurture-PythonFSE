-- ===========================
-- Hands-On 3 : Task 1
-- Advanced SQL - Subqueries
-- ===========================

-- 35. Students enrolled in more courses than the average
SELECT s.student_id, s.first_name, s.last_name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(e.course_id) >
(
    SELECT AVG(course_count)
    FROM
    (
        SELECT COUNT(*) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) AS avg_table
);

-- 36. Courses where all enrolled students received grade 'A'
SELECT c.course_name
FROM courses c
WHERE NOT EXISTS
(
    SELECT *
    FROM enrollments e
    WHERE e.course_id = c.course_id
      AND e.grade <> 'A'
);

-- 37. Highest paid professor in each department
SELECT p1.prof_name,
       p1.salary,
       d.dept_name
FROM professors p1
JOIN departments d
ON p1.department_id = d.department_id
WHERE p1.salary =
(
    SELECT MAX(p2.salary)
    FROM professors p2
    WHERE p2.department_id = p1.department_id
);

-- 38. Departments with average salary greater than 85000
SELECT dept_name, avg_salary
FROM
(
    SELECT d.dept_name,
           AVG(p.salary) AS avg_salary
    FROM departments d
    JOIN professors p
    ON d.department_id = p.department_id
    GROUP BY d.dept_name
) AS salary_table
WHERE avg_salary > 85000;
