class Product:
    __slots__ = ['name', 'kcal']

    def __init__(self, name: str, kcal: int) -> None:
        self.name = name
        self.kcal = kcal


class Recipe:
    __slots__ = ['name', 'how_to_cook', 'ingredients']

    def __init__(self, name: str, how_to_cook: str,
                 ingredients: list[Product] = None) -> None:
        self.name = name
        self.how_to_cook = how_to_cook
        self.ingredients = ingredients

    def __str__(self):
        return self.name
