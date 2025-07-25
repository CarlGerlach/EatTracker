from sqlalchemy import select, update, delete
from settings import Session,  engine
from settings import ingredient, ingredient_dto, ingredient_id_dto
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/addIngredient")
async def add_ingredient(ini_ingredient: ingredient_dto):

    with Session(engine) as session:
        stmt = select(ingredient).where(ingredient.name == ini_ingredient.name)
        result = session.execute(stmt).first()

        if result:
            return {"message": "Ingredient already exists"}

        else:
            new_set = ingredient(name=ini_ingredient.name,calories=ini_ingredient.calories,carbs=ini_ingredient.carbs,
                                 sugars=ini_ingredient.sugars,protein=ini_ingredient.protein)

            session.add(new_set)
            session.commit()
            return {"success": True,
                    "message": "Ingredient added"}


@app.delete("/deleteIngredient")
async def delete_ingredient(ingredient_to_delete: ingredient_id_dto):
    with Session(engine) as session:
        stmt = select(ingredient).where(ingredient.id == ingredient_to_delete.id)
        result = session.execute(stmt).first()

        if result:
            stmt = delete(ingredient).where(ingredient.id == ingredient_to_delete.id)
            session.execute(stmt)
            session.commit()

            return {"success": True,
                    "message": "Ingredient deleted"
                    }

        else:
            return {"success": False,
                "message": "Ingredient not found"}

@app.put("/updateIngredient")
async def update_ingredient(ingredient_to_update_id: ingredient_id_dto, ini_ingredient: ingredient_dto):
    with Session(engine) as session:
        stmt = select(ingredient).where(ingredient.id == ingredient_to_update_id.id)
        result = session.execute(stmt).first()

        if result:
            stmt = update(ingredient).where(ingredient.id == ingredient_to_update_id.id).values(
                name=ini_ingredient.name, calories=ini_ingredient.calories, carbs=ini_ingredient.carbs,
                sugars=ini_ingredient.sugars, protein=ini_ingredient.protein)

            session.execute(stmt)
            session.commit()

            return {"success": True,
                    "message": "Ingredient updated"}

        else:
            return {"success": False,
                    "message": "Ingredient not found"}

@app.get("/getIngredient")
async def get_ingredient(searched_ingredient: ingredient_id_dto):
    with Session(engine) as session:
        stmt = select(ingredient).where(ingredient.id == searched_ingredient.id)
