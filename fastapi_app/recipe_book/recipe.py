class Product:

    def __init__(self, name: str, kcal: int) -> None:
        self.name = name
        self.kcal = kcal

    def __str__(self):
        return self.name


class Recipe:

    def __init__(self, name: str, how_to_cook: str, cooking_time_in_min: int,
                 ingredients: list[Product] = None) -> None:
        self.name = name
        self.how_to_cook = how_to_cook
        self.cooking_time_in_min = cooking_time_in_min
        self.ingredients = ingredients

    def __str__(self):
        return self.name
