from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

fastapi = FastAPI()

class User(BaseModel):
    username: str
    password: str
    email: Optional[str] = None
    phone_number: Optional[int] = None

@fastapi.get("/")
async def root():
    return {"message: Welcome to my API"}

@fastapi.post("/createuser")
async def create_user(new_user: User):
    print(new_user)
    return {"message": "Successfully created user", "username": f"{new_user.username}", "email": f"{new_user.email}" }