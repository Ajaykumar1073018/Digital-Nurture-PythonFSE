-- ===========================
-- Hands-On 3 : Task 3
-- Stored Procedures & Transactions
-- ===========================

-- 44. Stored Procedure to Enroll Student
DELIMITER $$

CREATE PROCEDURE sp_enroll_student(
    IN p_student_id INT,
    IN p_course_id INT,
    IN p_date DATE
)
BEGIN

IF EXISTS
(
    SELECT *
    FROM enrollments
    WHERE student_id=p_student_id
    AND course_id=p_course_id
)
THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT='Duplicate Enrollment';
ELSE
    INSERT INTO enrollments(student_id,course_id,enrollment_date)
    VALUES(p_student_id,p_course_id,p_date);
END IF;

END$$
DELIMITER ;

-- 45. Create Log Table
CREATE TABLE department_transfer_log(
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    old_department INT,
    new_department INT,
    transfer_date DATE
);

-- Transaction Example
START TRANSACTION;

UPDATE students
SET department_id=2
WHERE student_id=1;

INSERT INTO department_transfer_log
(student_id,old_department,new_department,transfer_date)
VALUES
(1,1,2,CURDATE());

COMMIT;

-- 46. Rollback Example
START TRANSACTION;

UPDATE students
SET department_id=5
WHERE student_id=2;

ROLLBACK;

-- 47. SAVEPOINT Example
START TRANSACTION;

INSERT INTO enrollments(student_id,course_id,enrollment_date)
VALUES(2,2,CURDATE());

SAVEPOINT sp1;

-- Intentional duplicate
INSERT INTO enrollments(student_id,course_id,enrollment_date)
VALUES(2,2,CURDATE());

ROLLBACK TO sp1;

COMMIT;
