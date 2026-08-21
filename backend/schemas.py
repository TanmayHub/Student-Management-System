from pydantic import BaseModel, EmailStr, Field, field_validator,ConfigDict
from typing import Optional, Literal
from datetime import datetime

# Student Schema
class StudentBase(BaseModel):
    roll_no: str = Field(
        ...,
        min_length=3,
        max_length=20,
        description="Student Roll Number"
    )

    name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Student Name"
    )

    email: EmailStr

    phone: Optional[str] = Field(
        None,
        pattern=r"^\d{10}$",
        description="10 digit mobile number"
    )

    course: Optional[str] = Field(
        None,
        min_length=2,
        max_length=50
    )

    semester: Optional[int] = Field(
        None,
        ge=1,
        le=8
    )

    marks: Optional[float] = Field(
        None,
        ge=0,
        le=100
    )

    @field_validator("roll_no", "name", "course")
    @classmethod
    def remove_extra_spaces(cls, value):
        if value is None:
            return value

        value = value.strip()

        if not value:
            raise ValueError("Field cannot be empty.")

        return value


class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentBase):
    pass


class StudentResponse(StudentBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

# User Schema
class UserCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="User Name"
    )

    email: EmailStr

    password: str = Field(
        ...,
        min_length=8,
        max_length=100,
        description="User Password"
    )

    role: Literal["admin", "faculty", "student"]

    @field_validator("name")
    @classmethod
    def remove_extra_spaces(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("Field cannot be empty.")

        return value

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )

class Token(BaseModel): #login response schema
    access_token: str
    token_type: str