from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from pydantic import BaseModel


base = declarative_base() # creates a base class for a database model


url = "mysql+pymysql://root:password@localhost:3306/mydb"
engine = create_engine(url, echo=True)
session = Session(engine) #connection to database

#Classes

class ingredient(base):
    __tablename__ = 'ingredient'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    calories = Column(Integer)
    carbs = Column(Integer)
    sugars = Column(Integer)
    protein = Column(Integer)


class ingredient_dto(BaseModel):
    name: str
    calories: int
    carbs: int
    sugars: int
    protein: int

class ingredient_id_dto(BaseModel):
    id: int






base.metadata.create_all(engine)