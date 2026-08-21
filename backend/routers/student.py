from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from crud import student_crud
import schemas
from dependencies import get_db,get_current_user

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# Create Student
@router.post(
    "/",
    response_model=schemas.StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return student_crud.create_student(db, student)

# Get All Students
@router.get(
    "/",
    response_model=List[schemas.StudentResponse]
)
def get_students(
    db: Session = Depends(get_db)
):
    return student_crud.get_students(db)


# Get Student By ID
@router.get(
    "/{student_id}",
    response_model=schemas.StudentResponse
)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = student_crud.get_student(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return student

# Update Student
@router.put(
    "/{student_id}",
    response_model=schemas.StudentResponse,
    status_code=status.HTTP_200_OK,
    summary="Update Student",
    description="Update an existing student's information."
)
def update_student(
    student_id: int,
    student: schemas.StudentUpdate,
    db: Session = Depends(get_db)
):
        
    updated_student = student_crud.update_student(
        db,
        student_id,
        student
    )

    if updated_student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        ) # because it is a data base error not business error, so we didn't remove it

    return updated_student

    
# Delete Student
@router.delete(
    "/{student_id}",
    response_model=schemas.StudentResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete Student",
    description="Delete a student by their ID."
)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    
        deleted_student = student_crud.delete_student(
            db,
            student_id
        )

        if deleted_student is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found"
            )

        return deleted_student

    