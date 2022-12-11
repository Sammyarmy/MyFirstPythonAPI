from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    password: str
    email: Optional[str] = None
    phone_number: Optional[int] = None