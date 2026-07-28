-- ============================================================
-- HANDS-ON 1: SCHEMA DESIGN & CORE SQL - DDL and Normalisation
-- ============================================================
-- Name: Your Name
-- Date: 2026-07-02
-- Database: MySQL
-- Path: Python FSE/Database integration/YourName/hands_on_1.sql
-- ============================================================

-- Use the database
USE college_db;

-- Drop existing tables if they exist (in reverse order of dependencies)
DROP TABLE IF EXISTS professors;
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS departments;

-- ============================================================
-- TASK 1: CREATE TABLES
-- ============================================================

-- Create departments table
CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100) NOT NULL,
    hod_name VARCHAR(100) NOT NULL,
    budget DECIMAL(12,2)
);

-- Create students table
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_of_birth DATE,
    department_id INT,
    enrollment_year INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Create courses table
CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(150) NOT NULL,
    course_code VARCHAR(20) UNIQUE,
    credits INT,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Create enrollments table
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    grade CHAR(2),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    CONSTRAINT grade_check CHECK (grade IN ('A', 'B', 'C', 'D', 'F') OR grade IS NULL)
);

-- Create professors table
CREATE TABLE professors (
    professor_id INT PRIMARY KEY AUTO_INCREMENT,
    prof_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department_id INT,
    salary DECIMAL(10,2),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Verify tables created
SHOW TABLES;

-- ============================================================
-- TASK 2: VERIFY NORMALISATION
-- ============================================================

/*
===========================================
NORMALISATION ANALYSIS
===========================================

1NF (First Normal Form):
- All columns contain atomic (single) values
- No repeating groups or arrays
- Each row is uniquely identifiable
- Our schema satisfies 1NF

2NF (Second Normal Form):
- In 1NF, and all non-key columns depend on the ENTIRE primary key
- For enrollments table: (student_id, course_id) is the composite key
- grade depends on both student_id AND course_id
- enrollment_date also depends on both
- Therefore, 2NF is satisfied

3NF (Third Normal Form):
- In 2NF, and no transitive dependencies
- Transitive dependency: A -> B -> C (where C depends on B, not directly on A)
- Example: If we stored dept_name in students table, it would depend on department_id,
  which is a non-key column (foreign key), violating 3NF
- Our schema only stores department_id (foreign key), so 3NF is satisfied
- All non-key columns depend directly on the primary key

CONCLUSION: Our schema is in 3NF.
===========================================
*/

-- ============================================================
-- TASK 3: ALTER AND EXTEND SCHEMA
-- ============================================================

-- 10. Add phone_number column
ALTER TABLE students ADD COLUMN phone_number VARCHAR(15);

-- 11. Add max_seats column
ALTER TABLE courses ADD COLUMN max_seats INT DEFAULT 60;

-- 12. Add CHECK constraint for grade
ALTER TABLE enrollments ADD CONSTRAINT grade_check 
    CHECK (grade IN ('A', 'B', 'C', 'D', 'F') OR grade IS NULL);

-- 13. Rename hod_name to head_of_dept
ALTER TABLE departments CHANGE hod_name head_of_dept VARCHAR(100);

-- 14. Drop phone_number column (simulate rollback)
ALTER TABLE students DROP COLUMN phone_number;

-- ============================================================
-- VERIFY FINAL SCHEMA
-- ============================================================

-- Check table structures
DESCRIBE departments;
DESCRIBE students;
DESCRIBE courses;
DESCRIBE enrollments;
DESCRIBE professors;

-- ============================================================
-- EXPECTED OUTCOME:
-- ============================================================
-- All 5 tables created successfully
-- students table: no phone_number column (dropped)
-- departments table: head_of_dept column instead of hod_name
-- courses table: max_seats column with default 60
-- enrollments table: grade_check constraint applied
-- ============================================================