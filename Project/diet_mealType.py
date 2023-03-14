import pprint

import requests
from decouple import config
from user_input import ingredient

APP_ID = config('APP_ID')
APP_KEY = config('APP_KEY')
# Ask the user to enter an ingredient that they want to search for, ask extra question
meal_type = {'breakfast', 'lunch', 'snack', 'teatime', 'dinner'}
diet_restriction = {'balanced', 'high-fiber', 'low-carb', 'low-fat', 'low-sodium'}
has_diet = input('Are you On A Diet?? ')
if has_diet == 'yes':
    diet_input = input(f"Could you choose one of these choices: {diet_restriction}: ")
else:
    diet_input = None
has_meal_type = input('Are you looking for a particular meal type?? ')
if has_meal_type == 'yes':
    meal_type_input = input(f"Could tou choose one fo these meal types? {meal_type}: ")
else:
    meal_type_input = None


# Create a function that makes a request to the Edamam API with the required ingredient as
# part of the search query (also included your Application ID and Application Key
def extra_recipe_search(search_term, diet, meal_types):
    """
    :Purpose: Search for recipes from the web via an API.
    :param search_term: string - input chosen by user for a recipe.
    :param diet.
    :param meal_types.
    :return: a list of recipe(s) that match the search term by user.

    Function that takes search term input by user as
    an argument and returns a list of recipe(s) that match the search term.
    """
    # "https://api.edamam.com/api/recipes/v2?type=public&q=olives&app_id=2e66588b&app_key=94e8f7bfbc31d8515e397b83f366d84a&
    # ingr=5-8&diet=balanced&
    # health=alcohol-cocktail&cuisineType=American&mealType=Breakfast&dishType=Biscuits%20and%20cookies&calories=200-100"
    # ingr,diet,health,cuisineType,mealType,dishType,calories

    url = requests.get(f"https://api.edamam.com/api/recipes/v2?type=public&q={search_term}&app_id={APP_ID}&"
                       f"app_key={APP_KEY}&diet={diet}&mealType={meal_types}")

    data = url.json()
    # print(requests.get(url))
    # print(data['hits']['recipe']['label'])
    return data['hits']


def extra_parameters():
    recipe_list = extra_recipe_search(ingredient, diet_input, meal_type_input)
    for my_list in recipe_list:
        my_results = my_list['recipe']
        pprint.pprint("Name: {}\nThe Ingredients: {}\nMeal Type: {}\nDiet: {}\n"
                      .format(my_results['label'],
                              (my_results['ingredientLines']),
                              (my_results['mealType']),
                              my_results['dietLabels']))


extra_parameters()
