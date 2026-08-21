from fastapi import HTTPException

from security import hash_password,verify_password
from logger import logger
from sqlalchemy.orm import Session

import models
import schemas


# Create User
def create_user(db: Session, user: schemas.UserCreate):
    existing_user = get_user_by_email(db, user.email)

    if existing_user:
        logger.warning(
            f"Registration failed. Email already exists: {user.email}"
        )
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )
    
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

def get_user_by_email(db: Session, email: str):
    return (
        db.query(models.User)
        .filter(models.User.email == email)
        .first()
    )

def authenticate_user(db: Session,email: str,password: str):
    db_user = get_user_by_email(db, email)
    if not db_user:
        logger.warning(f"Login failed. User not found: {email}")
        return None
    if not verify_password(password, db_user.password):
        logger.warning(f"Login failed. Invalid password: {email}")
        return None

    logger.info(f"User authenticated successfully: {email}")
    return db_user