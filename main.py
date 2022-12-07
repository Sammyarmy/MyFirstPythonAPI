from fastapi import FastAPI

fastapi = FastAPI()

@fastapi.get("/")
async def root():
    return {"message: Welcome to my API"}

@fastapi.post("/createuser")
async def create_user():
    return {"message: Successfully created user"}