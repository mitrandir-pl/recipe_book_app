from fastapi import APIRouter, Depends
from pydantic import BaseModel

from config.db_settings import get_session
from recipe_book import Recipe
from DB import Neo4jSession

router = APIRouter()


class RecipeName(BaseModel):
    name: str = None


@router.get("/recipes_name")
async def get_recipes_by_name(recipe: RecipeName,
                              session: Neo4jSession = Depends(get_session)):
    recipes = session.get_recipe_by_name(
        recipe.name
    )
    return recipes
