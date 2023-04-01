class Product:

    def __init__(self, name: str, kcal: int) -> None:
        self.name = name
        self.kcal = kcal


class Recipe:

    def __init__(self, name: str, how_to_cook: str,
                 ingredients: list[Product] = None) -> None:
        self.name = name
        self.how_to_cook = how_to_cook
        self.ingredients = ingredients

    def __str__(self):
        return self.name
