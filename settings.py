from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import create_engine, Column, Integer, String


base = declarative_base() # creates a base class for a database model


url = "mysql+pymysql://root:password@localhost:3306/mydb"
engine = create_engine(url, echo=True)
session = Session(engine) #connection to database

#Classes

class ingredients(base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    energy = Column(Integer)
    carbs = Column(Integer)
    sugars = Column(Integer)
    protein = Column(Integer)




base.metadata.create_all(engine)