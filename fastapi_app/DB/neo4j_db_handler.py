from dataclasses import dataclass
import os

from neo4j import GraphDatabase, Driver

from recipe_book import Recipe, Product
from exceptions import (
    RecipeDoesNotExistException,
    NoIngredientsEnteredException,
    NoIngredientsException,
)


class Neo4jDatabaseHandler:

    def __init__(self, driver: Driver):
        self.driver = driver

    def get_recipes_from_data(self, data: dict) -> list[Recipe]:
        """Gets data from database and returns list of recipes from it."""
        if data:
            list_of_recipes = []
            for i in data:
                recipe_name = i['recipe']['name']
                recipe_how_to_cook = i['recipe']['how_to_cook']
                recipe_time = i['recipe']['cooking_time_in_min']
                ingredients = self.get_ingredients_for_recipe(
                    recipe_name
                )
                list_of_recipes.append(
                    Recipe(recipe_name, recipe_how_to_cook, recipe_time, ingredients)
                )
        else:
            raise RecipeDoesNotExistException()
        return list_of_recipes

    def get_recipes(self) -> list[Recipe]:
        """Returns a lisr with all recipes."""
        with self.driver.session() as session:
            recipe = session.execute_write(self._get_recipes)
        return recipe

    def _get_recipes(self, tx) -> list[Recipe]:
        """Finds and returns all recipes."""
        query = "MATCH (recipe:Recipe) RETURN recipe"
        data = tx.run(query).data()
        list_of_recipes = self.get_recipes_from_data(data)
        return list_of_recipes

    def get_recipe_by_name(self, recipe_name: str) -> Recipe:
        """Returns a recipe by name.

        Method gets recipe name, and finds this recipe in the database.
        If recipe is not exists, raising exception.

        :param recipe_name: name of the recipe we need to find
        :return: Recipe
        """
        with self.driver.session() as session:
            recipe = session.execute_write(self._get_recipe_by_name, recipe_name)
        return recipe

    def _get_recipe_by_name(self, tx, recipe_name: str) -> Recipe:
        """Finds and returns recipe by its name."""
        query = "MATCH (recipe:Recipe {name: $recipe_name}) RETURN recipe"
        data = tx.run(query, recipe_name=recipe_name).single()
        if data:
            recipe_name = data[0]['name']
            recipe_how_to_cook = data[0]['how_to_cook']
            recipe_time = data[0]['cooking_time_in_min']
            ingredients = self.get_ingredients_for_recipe(recipe_name)
            recipe = Recipe(recipe_name, recipe_how_to_cook, recipe_time, ingredients)
        else:
            raise RecipeDoesNotExistException()
        return recipe

    def get_recipes_by_country(self, country_name: str) -> list[Recipe]:
        """Returns a recipe by country.

        Method gets country name, and finds this recipe in the database.
        If recipe is not exists, raising exception.

        :param country_name: name of the country which recipes we need to find
        :return: list of found recipes
        """
        with self.driver.session() as session:
            recipe = session.execute_write(self._get_recipes_by_country, country_name)
        return recipe

    def _get_recipes_by_country(self, tx, country_name: str) -> list[Recipe]:
        """Finds and returns list of recipes by country."""
        query = "MATCH (recipe:Recipe)<-[:is_food_of]-" \
                "(country:Country {name: $country_name}) RETURN recipe"
        data = tx.run(query, country_name=country_name).data()
        list_of_recipes = self.get_recipes_from_data(data)
        return list_of_recipes

    def get_recipes_by_category(self, category_name: str) -> list[Recipe]:
        """Returns a recipe by category.

        Method gets category name, and finds this recipe in the database.
        If recipe is not exists, raising exception.

        :param category_name: name of the category which recipes we need to find
        :return: list of found recipes
        """
        with self.driver.session() as session:
            recipe = session.execute_write(self._get_recipes_by_category, category_name)
        return recipe

    def _get_recipes_by_category(self, tx, category_name: str) -> list[Recipe]:
        """Finds and returns list of recipes by category."""
        query = "MATCH (recipe:Recipe)<-[:INCLUDE]-" \
                "(category:FoodCategory {name: $category_name}) RETURN recipe"
        data = tx.run(query, category_name=category_name).data()
        list_of_recipes = self.get_recipes_from_data(data)
        return list_of_recipes

    def get_recipes_by_country_category_and_time(self, country_name: str,
                                                 category_name: str,
                                                 cooking_time_in_min: int) -> list[Recipe]:
        """Returns a recipe by category, country and cooking time.

        Method gets category name, country name and time,
        and searching for recipes in the database.
        If recipe is not exists, raising exception.

        :param country_name: name of the country which recipes we need to find
        :param category_name: name of the category which recipes we need to find
        :param cooking_time_in_min: time that user has for cooking
        :return: list of found recipes
        """
        with self.driver.session() as session:
            recipe = session.execute_write(
                self._get_recipes_by_country_category_and_time,
                country_name, category_name, cooking_time_in_min
            )
        return recipe

    def _get_recipes_by_country_category_and_time(self, tx, country_name: str,
                                                  category_name: str,
                                                  cooking_time_in_min: int) -> list[Recipe]:
        """Finds and returns list of recipes by country, category and time."""
        query = "MATCH (country:Country {name: $country_name})-[:is_food_of]->" \
                "(recipe:Recipe)<-[:INCLUDE]-" \
                "(category:FoodCategory {name: $category_name})" \
                "WHERE recipe.cooking_time_in_min < $cooking_time_in_min " \
                "RETURN recipe"
        data = tx.run(query, country_name=country_name,
                      category_name=category_name, cooking_time_in_min=cooking_time_in_min).data()
        list_of_recipes = self.get_recipes_from_data(data)
        return list_of_recipes

    def get_recipe_by_ingredients(self, ingredients: list) -> list[Recipe]:
        """Returns a recipe by ingredients.

        Method gets ingredients, and tries to find
        recipes with this ingredients in database.
        If recipes are not exists, raising exception.

        :param ingredients: list of ingredients
        :return: list of found recipes
        """
        with self.driver.session() as session:
            list_of_recipes = session.execute_write(
                self._get_recipe_by_ingredients, ingredients
            )
        breakpoint()
        return list_of_recipes

    def _get_recipe_by_ingredients(self, tx, ingredients: list) -> list[Recipe]:
        """Finds and returns recipe by ingredients."""
        query = self._get_query_for_recipe_by_ingredients(ingredients)
        data = tx.run(query).data()
        list_of_recipes = self.get_recipes_from_data(data)
        return list_of_recipes

    def _get_query_for_recipe_by_ingredients(self, ingredients: list) -> str:
        """Returns query string for the search by ingredients."""
        if not ingredients:
            raise NoIngredientsEnteredException()
        query = f'CALL {{MATCH (recipe:Recipe)-[:INGREDIENT]->' \
                f'(:Product {{name: "{ingredients[0]}"}})'
        if len(ingredients) > 1:
            for index, i in enumerate(ingredients[1:], start=1):
                query += f', (recipe)-[:INGREDIENT]->' \
                         f'(:Product {{name: "{ingredients[index]}"}})'
        query += "RETURN recipe} MATCH (recipe)-[:INGREDIENT]->" \
                 "(product:Product) RETURN DISTINCT recipe, product"
        return query

    def get_ingredients_for_recipe(self, recipe_name: str) -> list[Product]:
        """Returns list of ingredients for rhe recipe.

        Method gets a recipe name and makes a query to the database
        to find ingredients for this recipe. If there are no ingredients,
        raising exception. Else, returning list of ingredients.

        :param recipe_name: name of the recipe
        :return: list of ingredients
        """
        with self.driver.session() as session:
            recipe = session.execute_write(self._get_ingredients_for_recipe, recipe_name)
        return recipe

    def _get_ingredients_for_recipe(self, tx, recipe_name: str) -> list[Product]:
        """Finds and returns ingredients needed for a recipe."""
        query = "MATCH (:Recipe {name: $recipe_name})-[:INGREDIENT]->" \
                "(ingredients:Product) RETURN ingredients"
        data = tx.run(query, recipe_name=recipe_name).data()
        if data:
            ingredients = []
            for i in data:
                ingredient = Product(
                    i['ingredients']['name'],
                    i['ingredients']['calories_per_100_grams'],
                )
                ingredients.append(ingredient)
        else:
            raise NoIngredientsException()
        return ingredients

    def count_calories_in_recipe(self):
        pass


@dataclass
class Neo4jSession:
    driver: Driver = None

    def __enter__(self) -> Neo4jDatabaseHandler:
        """Establishes a connection with the database.

        :return: None
        """
        self.driver = GraphDatabase.driver(
            os.getenv("NEO4J_URI"),
            auth=(os.getenv("NEO4J_USERNAME"),
                  os.getenv("NEO4J_PASSWORD"))
        )
        return Neo4jDatabaseHandler(self.driver)

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Closes connection with database."""
        self.driver.close()
