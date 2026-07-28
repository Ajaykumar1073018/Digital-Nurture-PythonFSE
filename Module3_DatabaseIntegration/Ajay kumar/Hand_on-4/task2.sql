-- ===========================
-- Hands-On 4 : Task 2
-- Add Indexes and Compare Plans
-- ===========================

-- 51. Create index on enrollment_year
CREATE INDEX idx_students_enrollment_year
ON students(enrollment_year);

-- 52. Composite UNIQUE index
CREATE UNIQUE INDEX idx_enrollment_unique
ON enrollments(student_id, course_id);

-- 53. Index on course_code
CREATE INDEX idx_course_code
ON courses(course_code);

-- 54. Run EXPLAIN again
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

-- Comments:
-- After creating indexes, EXPLAIN should show
-- Index Scan (PostgreSQL) or Index Lookup (MySQL)
-- instead of a Full Table Scan where applicable.

-- 55. Partial Index (PostgreSQL)
CREATE INDEX idx_null_grades
ON enrollments(student_id)
WHERE grade IS NULL;

-- For MySQL (Partial indexes are not supported)
-- Use a normal index instead:
-- CREATE INDEX idx_null_grades
-- ON enrollments(student_id);
