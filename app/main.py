from typing import Optional
from fastapi import Depends, FastAPI, status, HTTPException
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session
from .database import models
from .database.database import engine, get_db

fastapi = FastAPI()

get_db()
models.Base.metadata.create_all(bind=engine)

class User(BaseModel):
    username: str
    password: str
    email: Optional[str] = None
    phone_number: Optional[int] = None

@fastapi.get("/")
def root():
    return {"message: Welcome to my API"}

@fastapi.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(new_user: User, db: Session = Depends(get_db)):
    user = models.User(username=new_user.username, password=new_user.password, email=new_user.email, phone_number=new_user.phone_number)
    db.add(user)
    db.commit()
    db.refresh(user)
    return { "message": "New User created", "user_info": user}

@fastapi.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"No users found")
    return {"users": users}

@fastapi.get("/users/{username}")
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"user '{username}' not found")
    return {"user": user}