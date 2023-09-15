from typing import List
from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()

# Helper function to get database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()



@app.post("/api", response_model=schemas.Person, status_code=status.HTTP_201_CREATED)
def create_user(person: schemas.PersonCreate, session: Session = Depends(get_session)):
    
    #check if user with given name already exists in the db and return a 400 if true
    dbperson = session.query(models.Person).get(person.name)
    if dbperson:
        raise HTTPException(status_code=400, detail = f"user with name {person.name} already exists")
    
    # create an instance of the Person database model
    persondb = models.Person(name = person.name)


    # add it to the session and commit it
    session.add(persondb)
    session.commit()
    session.refresh(persondb)

    # return the person object
    return persondb

@app.get("/api/{user_id}", response_model=schemas.Person)
def read_user(name: str, session: Session = Depends(get_session)):

    # get the person item with the given id
    person = session.query(models.Person).get(name)

    # check if person item with given id exists. If not, raise exception and return 404 not found response
    if not person:
        raise HTTPException(status_code=404, detail=f"person with name {name} not found")

    return person

@app.put("/api/{user_id}", response_model=schemas.Person)
def update_user(name: str, email: str, age: str, session: Session = Depends(get_session)):

    # get the person item with the given id
    person = session.query(models.Person).get(name)

    # update person item with the given id (if an item with the given id was found)
    if person:
        person.name = name
        person.email = email
        person.age = age
        session.commit()

    # If not, raise exception and return 404 not found response
    if not person:
        raise HTTPException(status_code=404, detail=f"person with name {name} not found")

    return person

@app.delete("/api/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(name: str, session: Session = Depends(get_session)):

    # get the person item with the given id
    person = session.query(models.Person).get(name)

    # if person item with given id exists, delete it from the database. Otherwise raise 404 error
    if person:
        session.delete(person)
        session.commit()
        
    else:
        raise HTTPException(status_code=404, detail=f"person with name {name} not found")

    return HTTPException(status_code=204, detail= "delete succesfull")

@app.get("/api", response_model = List[schemas.Person])
def read_user_list(session: Session = Depends(get_session)):

    # get all person items
    person_list = session.query(models.Person).all()

    return person_list