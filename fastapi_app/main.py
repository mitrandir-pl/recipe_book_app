import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from DB import DatabaseHandler, Neo4jDatabaseHandler, Neo4jSession
from routes import recipes_urls

app = FastAPI()
app.include_router(recipes_urls.router)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def connect_to_database(database_handler: DatabaseHandler,
                        uri: str, username: str, password: str) -> None:
    database_handler.connect(uri, username, password)


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
    return list_of_recipes


load_dotenv()


@app.get("/")
def read_root():
    with Neo4jSession() as session:
        session.get_recipes_by_country_category_and_time(
        'Italy', 'Second course', 65
    )
    # print(len(main()))
    # for i in main():
    #     print(i)
    # breakpoint()
    return {"id": 1}
