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

@fastapi.post("/users")
async def create_user(new_user: User):
    print(new_user)
    return { "message": "New User created", "user_info": new_user.dict() }