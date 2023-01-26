from typing import Any
import requests
from decouple import config

APP_ID = config('APP_ID')
APP_KEY = config('APP_KEY')


# Create a function that makes a request to the Edamam API with the required ingredient as
# part of the search query (also included your Application ID and Application Key
def recipe_search(search_term, meal_type, diet):
    """
    :Purpose: Search for recipes from the web via an API.
    :param search_term: string - input chosen by user for a recipe.
    :param meal_type
    :param diet
    :return: a list of recipe(s) that match the search term by user.

    Function that takes search term input by user as
    an argument and returns a list of recipe(s) that match the search term.
    """
    # "https://api.edamam.com/api/recipes/v2?type=public&q=olives&app_id=2e66588b&app_key=94e8f7bfbc31d8515e397b83f366d84a&
    # ingr=5-8&diet=balanced&
    # health=alcohol-cocktail&cuisineType=American&mealType=Breakfast&dishType=Biscuits%20and%20cookies&calories=200-100"
    # ingr,diet,health,cuisineType,mealType,dishType,calories
    url = requests.get('https://api.edamam.com/api/recipes/v2',
                       headers={'Accept': 'application/json'},
                       params={
                           'app_id': APP_ID,
                           'app_key': APP_KEY,
                           'q': search_term,
                       })

    data = url.json()
    # print(requests.get(url))
    # print(data['hits']['recipe']['label'])
    print(data)
    return data['hits']
