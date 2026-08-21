from logger import logger
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError

from database import engine
from models import Base
from routers import student
from routers import auth

from exceptions import (
    http_exception_handler,
    integrity_error_handler,
    validation_exception_handler,
    general_exception_handler
)

app = FastAPI(
    title="Student Management System API"
)

logger.info("Student Management System API started.")

# Register Global Exception Handlers
app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

app.add_exception_handler(
    IntegrityError,
    integrity_error_handler
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.add_exception_handler(
    Exception,
    general_exception_handler
)

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

app.include_router(student.router)

app.include_router(auth.router)


@app.get("/")
def home():
    return {
        "message": "Student Management System Backend is Running!"
    }