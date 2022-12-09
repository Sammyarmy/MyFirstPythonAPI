from app.models import User
from .setup import engine
from .db_models import db_User
from sqlalchemy.orm import Session

def db_create_user(new_user: User, db: Session):
    user = db_User(username=new_user.username, password=new_user.password, email=new_user.email, phone_number=new_user.phone_number)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def db_get_users(db: Session):
    user = db.query(db_User).all()
    return user

def db_get_user(username:str, db: Session):
    user = db.query(db_User).filter(db_User.username == username).first()
    return user