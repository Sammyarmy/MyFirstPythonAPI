from sqlalchemy import TIMESTAMP, Column, Integer, String, text
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False, unique=False)
    email = Column(String, nullable=True, unique=True)
    phone_number = Column(Integer,  nullable=True, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))