from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .crud import get_user_by_email_query, create_user_query
from .database import SessionLocal, engine

# table作成
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    """Dependency"""
    try:
        db = SessionLocal()  # sessionを生成
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email_query(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user_query(db=db, user=user)
