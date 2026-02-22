from .spellbook import record_spell # noqa


def validate_ingredients(ingredients: str) -> str:
    valids: tuple[str, str, str, str] = ("fire", "water", "earth", "air")
    ingredients_split: list[str] = ingredients.split(" ")
    for ingredient in ingredients_split:
        if ingredient not in valids:
            return ingredients + " - INVALID"
    return ingredients + " - VALID"
