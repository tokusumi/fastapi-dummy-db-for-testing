from sqlalchemy.orm import Session
from hashlib import md5 as hash_func
from . import models
from . import schemas


def get_user_by_email_query(db: Session, email: str):
    """get user by email"""
    return db.query(models.User).filter(models.User.email == email).first()


def create_user_query(db: Session, user: schemas.UserCreate):
    """create user by email and password"""
    hashed_password = hash_func(user.password.encode()).hexdigest()
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
