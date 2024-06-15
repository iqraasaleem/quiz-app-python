from fastapi import FastAPI
from quiz_backend.db.db_connector import get_session,createTable 
from quiz_backend.models.user_models import User 

async def lifeSpan(app: FastAPI):
     createTable()
     print("create table...")
     yield


app =FastAPI(lifespan=lifeSpan)

@app.get("/")
def home():
     return "welcome to quiz project..."