from fastapi import Body, FastAPI

fastapi = FastAPI()

@fastapi.get("/")
async def root():
    return {"message: Welcome to my API"}

@fastapi.post("/createuser")
async def create_user(body: dict = Body(...)):
    print(body)
    return {"message": "Successfully created user", "username": f"{body['username']}" }