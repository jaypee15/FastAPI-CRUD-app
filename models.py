from sqlalchemy import Column, Integer, String
from database import Base

# Define Person class inheriting from Base
class Person(Base):
    __tablename__ = 'person'
    name = Column(String, primary_key=True, unique=True)
    email = Column(String, default="user@gmail.com")
    age = Column(String, default="22")