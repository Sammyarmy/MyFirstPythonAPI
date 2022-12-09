from fastapi import Depends, FastAPI, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.models import User
from .database.commands import db_create_user, db_get_users, db_get_user
from .database import db_models
from .database.setup import engine, get_db

fastapi = FastAPI()

get_db()
db_models.Base.metadata.create_all(bind=engine)


@fastapi.get("/")
def root():
    return {"message: Welcome to my API"}

@fastapi.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(new_user: User, db: Session = Depends(get_db)):
    print(new_user)
    user = db_create_user(new_user, db)
    return { "message": "New User created", "user_info": user}

@fastapi.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db_get_users(db)
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"No users found")
    return {"users": users}

@fastapi.get("/users/{username}")
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    user = db_get_user(username, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"user '{username}' not found")
    return {"user": user}