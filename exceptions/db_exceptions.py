class RecipeDoesNotExistException(Exception):

    def __init__(self):
        super().__init__("No such recipe in database.")


class NoIngredientsEnteredException(Exception):
    def __init__(self):
        super().__init__("You didn't entered any ingredients.")


class NoIngredientsException(Exception):
    def __init__(self):
        super().__init__("This recipe has no ingredients.")
