from database import SessionLocal

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from auth import oauth2_scheme, decode_access_token
from crud import user_crud


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    payload = decode_access_token(token)

    credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)
    if payload is None:
        raise credentials_exception

    email = payload.get("sub")

    if email is None:
        raise credentials_exception

    db_user = user_crud.get_user_by_email(db, email)

    if db_user is None:
        raise credentials_exception

    return db_user