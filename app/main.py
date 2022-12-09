from typing import Optional
from xml.dom.minidom import TypeInfo
from fastapi import Body, FastAPI, status, HTTPException
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time

fastapi = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='MyFirstPythonAPI', user='postgres', password='password123', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection successful")
        break
    except Exception as error:
        print(f"Database connection failed, error: {error}")
        time.sleep(2)

class User(BaseModel):
    username: str
    password: str
    email: Optional[str] = None
    phone_number: Optional[int] = None

@fastapi.get("/")
def root():
    return {"message: Welcome to my API"}

@fastapi.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(new_user: User):
    cursor.execute("""INSERT INTO users (username, password, email, phone_number) VALUES (%s, %s, %s, %s)
     RETURNING * """,
     (new_user.username, new_user.password, new_user.email, new_user.phone_number))
    user = cursor.fetchall()
    conn.commit()
    return { "message": "New User created", "user_info": user}

@fastapi.get("/users")
def get_users():
    cursor.execute("""SELECT * FROM users """)
    users = cursor.fetchall()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"No users found")
    return {"users": users}

@fastapi.get("/users/{username}")
def get_user_by_username(username: str):
    print(username)
    print(type(username))
    cursor.execute("""SELECT * FROM users WHERE username = %s""", (username,))
    user = cursor.fetchall()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"user '{username}' not found")
    return {"user": user}