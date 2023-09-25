from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as PyEnum
from app.config.database import Base



class UserRole(str, PyEnum):
    admin = "admin"
    superuser = "superuser"
    customer = "customer"
    usertype1 = "usertype1"
    usertype2 = "usertype2"
    
    
    
class loginMethod(str, PyEnum):
    email = "email"
    mobile = "mobile"
    username = "username"



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String)
    mobile = Column(String)
    role = Column(Enum(UserRole))