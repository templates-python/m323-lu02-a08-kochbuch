"""Kochbuch.

Aufgabenstellung: https://wiki.bzz.ch/modul/m323/learningunits/lu02/aufgaben/kochbuch
"""

# Dein Code kommt hier hin
import json


def adjust_recipe(original_recipe, num_people):
    """
    Adjusts the recipe based on the number of people.

    Parameters:
        original_recipe (dict): The original recipe.
        num_people (int): The number of people to adjust the recipe for.

    Returns:
        dict: The adjusted recipe.
    """
    adjusted_ingredients = {}
    original_servings = original_recipe['servings']
    factor = num_people / original_servings

    for ingredient, amount in original_recipe['ingredients'].items():
        adjusted_ingredients[ingredient] = amount * factor

    adjusted_recipe = {
        'title': original_recipe['title'],
        'ingredients': adjusted_ingredients,
        'servings': num_people,
    }
    return adjusted_recipe


def load_recipe(json_string):
    """
    Loads a recipe from a JSON string.

    Parameters:
        json_string (str): The JSON string containing the recipe.

    Returns:
        dict: The recipe as a Python dictionary.
    """
    return json.loads(json_string)


if __name__ == '__main__':
    # Example JSON string for a recipe
    recipe_json = (
        '{"title": "Spaghetti Bolognese", '
        '"ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, '
        '"servings": 4}'
    )
    # Convert JSON string to Python dictionary
    demo_original_recipe = load_recipe(recipe_json)
    # Adjust the recipe for 2 people
    demo_adjusted_recipe = adjust_recipe(demo_original_recipe, 8)
    print(f'Original Recipe: {demo_original_recipe}')
    print(f'Adjusted Recipe: {demo_adjusted_recipe}')
