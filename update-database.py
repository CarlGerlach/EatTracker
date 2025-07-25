from settings import Session, ingredient, engine


with Session(engine) as session:

    new_set = ingredient(name="Egg", calories=100,carbs=110,sugars=120,protein=130)
    session.add(new_set)
    session.commit()




