DELETE FROM `student_management`.`students` WHERE (`id` = '1');
DELETE FROM `student_management`.`students` WHERE (`id` = '2');
DELETE FROM `student_management`.`students` WHERE (`id` = '3');
DELETE FROM `student_management`.`students` WHERE (`id` = '8');

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'faculty', 'student') NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELETE FROM `student_management`.`students` WHERE (`id` = '11');
