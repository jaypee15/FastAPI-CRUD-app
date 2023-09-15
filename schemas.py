from pydantic import BaseModel

# Create Person Schema (Pydantic Model)
class PersonCreate(BaseModel):
    name: str
    

# Complete Person Schema (Pydantic Model)
class Person(PersonCreate):
    email:str
    age:str

    class Config:
        orm_mode = True