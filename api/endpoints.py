from fastapi import FastAPI, status, HTTPException
from pydantic_models import UserModel
from helper import execute_query
import psycopg2


app = FastAPI()


@app.post("/users", status_code = status.HTTP_201_CREATED)
def create_user(user: UserModel):
    if "@" not in user.email:
        raise HTTPException(status_code=400, detail="Invalid email")
    
    query = "INSERT INTO users (full_name, email, phone) VALUES (%s, %s, %s)"
    values = (user.full_name, user.email, user.phone)
    execute_query(query, values)

    return {"status": "success", "data": user}