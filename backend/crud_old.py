from security import hash_password
from logger import logger
from sqlalchemy.orm import Session

import models
import schemas


# Create Student
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.model_dump())

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    logger.info(
        f"Student created successfully | ID={db_student.id} | Roll No={db_student.roll_no}"
    )

    return db_student


# Get All Students
def get_students(db: Session):
    students = db.query(models.Student).all()

    logger.info(
    f"Retrieved {len(students)} students."
    )

    return students

# Get Student By ID
def get_student(db: Session, student_id: int):
    student = (
    db.query(models.Student)
    .filter(models.Student.id == student_id)
    .first()
)

    if student:
        logger.info(
            f"Retrieved student | ID={student_id}"
        )

    return student

# Update Student
def update_student(db: Session, student_id: int, student: schemas.StudentUpdate):
    db_student = (
        db.query(models.Student)
        .filter(models.Student.id == student_id)
        .first()
    )

    if db_student is None:
        return None

    for key, value in student.model_dump().items():
        setattr(db_student, key, value)

    db.commit()
    db.refresh(db_student)
    logger.info(f"Student updated successfully. ID={student_id}")

    return db_student


# Delete Student
def delete_student(db: Session, student_id: int):
    db_student = (
        db.query(models.Student)
        .filter(models.Student.id == student_id)
        .first()
    )

    if db_student is None:
        return None

    db.delete(db_student)
    db.commit()
    logger.info(f"Student deleted successfully. ID={student_id}")

    return db_student

# Create User
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)

    db_user = models.User(
    name=user.name,
    email=user.email,
    password=hashed_password,
    role=user.role
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    logger.info(
    f"User registered successfully | ID={db_user.id} | Email={db_user.email}"
    )
    return db_user