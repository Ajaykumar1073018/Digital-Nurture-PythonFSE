-- ===========================
-- Hands-On 4 : Task 1
-- Baseline Performance (No Indexes)
-- ===========================

-- 48. Run EXPLAIN on the query
EXPLAIN
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

-- 49 & 50. Analysis Comments

-- The EXPLAIN output shows the execution plan.
-- Before adding indexes, MySQL/PostgreSQL may perform
-- a Full Table Scan (MySQL) or Sequential Scan (PostgreSQL).
-- This is acceptable for small tables but becomes slower
-- as the amount of data increases.
-- Record the estimated cost or rows examined from your EXPLAIN output.
