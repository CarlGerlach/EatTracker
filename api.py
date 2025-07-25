from sqlalchemy import Engine

from settings import Session,  engine
from settings import ingredient, ingredient_dto
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/addIngredient")
async def add_ingredient(ini_ingredient: ingredient_dto):
    return {"message": "Hello Worlde"}

