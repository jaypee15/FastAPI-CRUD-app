# FastAPI CRUD Project

![Python 3](https://img.shields.io/badge/Python-3-green.svg?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-009485?style=for-the-badge&logo=fastapi&logoColor=white)

A simple REST API capable of CRUD operations on a "person" resource, built with FastAPI, SQLAlchemy and a SQLite db.  The API can be extended to use other databases easily. <a href="https://fastapi.tiangolo.com/tutorial/sql-databases/">Refer to this</a> for more information on how to use other databases with FastAPI.
 

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
-

## Prerequisites

List any prerequisites or dependencies that users need to have before they can use your application. For example:

- Python 3.7+
- Any IDE of choice
- Basic Python Knowledge
- Little of API design

## Getting Started

Follow the intstructions below to get started with the project

### Installation

 Clone the repository and install requirements:

   ```
    git clone <repository_url>

    pip install -r requirements.txt
   ```

  

### Run the application

    `uvicorn main:app --reload`

### API Endpoints


- POST /api: Create a new user.
- GET /api/{user_id}: Retrieve user details by name.
- PUT /api/{user_id}: Update user details by name.
- DELETE /api/{user_id}: Delete a user by name.
- GET /api: Retrieve a list of all users.

### Usage
- Get all the users present in the database, send a get request on the following endpoint:

```
http://127.0.0.1:8000/api
```
example respone: 
```
[
  {
    "name": "string",
    "email": "string",
    "age": "string"
  }
]
```
- To create a new user in the database, send a post request to the following endpoint:

```
http://127.0.0.1:8000/api
```
example request body: 
```
{
  "name": "string"
}
```
- To get a specific user's details in the database, send a get request to the following endpoint:
```
http://127.0.0.1:8000/api/{user_id}
```
example response: 
```
{
  "name": "string",
  "email": "string",
  "age": "string"
}
```
- To update a specific user's data, send a put request to the following endpoint:

```
http://127.0.0.1:8000/api/{user_id}
```
example request body: 
```
{
  "name": "string",
  "email": "string",
  "age": "string"
}
```

- To delete a user from the database, send a delete request to the following endpoint:
```
http://127.0.0.1:8000/api/{user_id}
```

example request: 
```
"string"
```
For further details, you can refer to <a href="http://127.0.0.1:8000/docs">http://127.0.0.1:8000/docs</a> after starting the server. This  will give you a very detailed documentation.


