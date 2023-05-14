from fastapi import APIRouter, Depends, UploadFile, File, Form
from pydantic import BaseModel

from config.db_settings import get_session
from DB import Neo4jSession

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
                              session: Neo4jSession = Depends(get_session)):
    """Returns a recipe by name"""
    recipes = session.get_recipe_by_name(recipe.name)
    return recipes


@router.get("/recipes_country")
async def get_recipes_by_name(recipe: RecipeCountry,
                              session: Neo4jSession = Depends(get_session)):
    """Returns a recipe by name"""
    recipes = session.get_recipe_by_name(recipe.country)
    return recipes


@router.post("/recipes_add")
async def post_new_recipe(recipe: Recipe,
                          session: Neo4jSession = Depends(get_session)):
    session.add_recipe(recipe)


@router.get("/recipes")
async def get_recipes(session: Neo4jSession = Depends(get_session)):
    """Returns all recipes from database"""
    recipes = session.get_recipes()
    return recipes
