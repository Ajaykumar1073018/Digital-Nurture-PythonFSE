-- ===========================
-- Hands-On 3 : Task 2
-- Views
-- ===========================

-- 39. Create Student Enrollment Summary View
CREATE VIEW vw_student_enrollment_summary AS
SELECT
    s.student_id,
    CONCAT(s.first_name,' ',s.last_name) AS student_name,
    d.dept_name,
    COUNT(e.course_id) AS total_courses,
    AVG(
        CASE
            WHEN e.grade='A' THEN 4
            WHEN e.grade='B' THEN 3
            WHEN e.grade='C' THEN 2
            WHEN e.grade='D' THEN 1
            WHEN e.grade='F' THEN 0
        END
    ) AS GPA
FROM students s
JOIN departments d
ON s.department_id=d.department_id
LEFT JOIN enrollments e
ON s.student_id=e.student_id
GROUP BY s.student_id,student_name,d.dept_name;

-- 40. Create Course Statistics View
CREATE VIEW vw_course_stats AS
SELECT
    c.course_name,
    c.course_code,
    COUNT(e.student_id) AS total_enrollments,
    AVG(
        CASE
            WHEN e.grade='A' THEN 4
            WHEN e.grade='B' THEN 3
            WHEN e.grade='C' THEN 2
            WHEN e.grade='D' THEN 1
            WHEN e.grade='F' THEN 0
        END
    ) AS avg_gpa
FROM courses c
LEFT JOIN enrollments e
ON c.course_id=e.course_id
GROUP BY c.course_name,c.course_code;

-- 41. Students with GPA above 3.0
SELECT *
FROM vw_student_enrollment_summary
WHERE GPA > 3.0;

-- 42. Try updating the view
UPDATE vw_student_enrollment_summary
SET GPA = 4
WHERE student_id = 1;

-- Comment:
-- Multi-table views generally cannot be updated because
-- SQL cannot determine which underlying table should be modified.

-- 43. Drop Views
DROP VIEW vw_course_stats;
DROP VIEW vw_student_enrollment_summary;

-- Recreate single-table view with CHECK OPTION
CREATE VIEW vw_student_enrollment_summary AS
SELECT student_id,
       first_name,
       last_name,
       enrollment_year
FROM students
WHERE enrollment_year >= 2022
WITH CHECK OPTION;
