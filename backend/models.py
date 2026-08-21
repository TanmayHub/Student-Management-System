from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DECIMAL
from sqlalchemy import TIMESTAMP
from sqlalchemy import text

from database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    roll_no = Column(String(20), unique=True, nullable=False)

    name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    phone = Column(String(15))

    course = Column(String(50))

    semester = Column(Integer)

    marks = Column(DECIMAL(5, 2))

    created_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP")
    )

from sqlalchemy import Column, Integer, String, Boolean, Enum, TIMESTAMP, text

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    role = Column(
        Enum("admin", "faculty", "student", name="user_roles"),
        nullable=False
    )
    is_active = Column(Boolean, default=True)
    created_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP")
    )