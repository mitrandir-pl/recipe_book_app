from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from DB.db_settings import get_session
from DB import Neo4jDatabaseHandler
from exceptions import RecipeDoesNotExistException
from routes import constants


router = APIRouter()


class RecipeName(BaseModel):
    name: str


class Recipe(BaseModel):
    recipe_name: str
    ingredients: dict
    category: str
    cooking_time: int
    recipe: str


class RecipeCountry(BaseModel):
    country: str


@router.post("/recipes_name")
async def get_recipes_by_name(recipe: RecipeName,
                              session: Neo4jDatabaseHandler = Depends(get_session)):
    """Returns a recipe by name"""
    recipes = session.get_recipe_by_name(recipe.name)
    return recipes


@router.get("/recipes_country")
async def get_recipes_by_name(recipe: RecipeCountry,
                              session: Neo4jDatabaseHandler = Depends(get_session)):
    """Returns a recipe by name"""
    try:
        recipes = session.get_recipe_by_name(recipe.country)
        return recipes
    except RecipeDoesNotExistException:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "")


@router.post("/recipes_add")
async def post_new_recipe(recipe: Recipe,
                          session: Neo4jDatabaseHandler = Depends(get_session)):
    session.add_recipe(recipe)


@router.get("/recipes")
async def get_recipes(session: Neo4jDatabaseHandler = Depends(get_session)):
    """Returns all recipes from database"""
    try:
        recipes = await session.get_recipes()
        return recipes
    except RecipeDoesNotExistException:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, constants.NO_RECIPES_IN_DB)
