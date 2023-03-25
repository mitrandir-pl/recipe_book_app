import os

from dotenv import load_dotenv

from UI import UIHandler
from fastapi_app.DB import DatabaseHandler, Neo4jDatabaseHandler


def connect_to_database(database_handler: DatabaseHandler,
                        uri: str, username: str, password: str) -> None:
    database_handler.connect(uri, username, password)


def start_ui(ui_handler: UIHandler) -> None:
    ui_handler.run()


def main():
    database_handler = Neo4jDatabaseHandler()
    connect_to_database(database_handler,
                        os.getenv("NEO4J_URI"),
                        os.getenv("NEO4J_USERNAME"),
                        os.getenv("NEO4J_PASSWORD"))
    # start_ui(DesktopUIHandler(database_handler))
    # name = database_handler.get_recipe_by_name("Borscht with chicken")
    # print(name)
    # list_of_recipes = database_handler.get_recipe_by_ingredients(['butter', 'sugar'])
    # for i in list_of_recipes:
    #     print(i)

    # list_of_recipes = database_handler.get_recipes_by_country('Italy')
    # for i in list_of_recipes:
    #     print(i)

    # list_of_recipes = database_handler.get_recipes_by_category('Second course')
    # for i in list_of_recipes:
    #     print(i)

    list_of_recipes = database_handler.get_recipes_by_country_category_and_time(
        'Italy', 'Second course', 65
    )
    for i in list_of_recipes:
        print(i)


if __name__ == "__main__":
    load_dotenv()
    main()
