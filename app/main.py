#main.py

from fastapi import FastAPI
from starlette.responses import RedirectResponse 

#config file
from app.config import config

#databse
import app.models.userModel as models #usermodel
from .config.database import engine

#routing
from .api.myApi import router as apiRouter


# app is instance of the class FastAPI 
app = FastAPI()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/")
async def welcome():
    return {"Greeting":"Hello World"}


@app.get("/intro")
async def my_intro():
    return {"Name":"Ajit kumar", "Age":21, "Country":"India", "Profession":"Software Engineer", "Languages":"Python, C++, C#", "Interests":"Football, Movies, Music", "Hobbies":"Coding, Reading, Travelling"}


models.Base.metadata.create_all(bind=engine)

#router for different api
app.include_router(apiRouter)