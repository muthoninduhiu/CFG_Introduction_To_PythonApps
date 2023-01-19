import requests
from decouple import config

APP_ID = config('APP_ID')
APP_KEY = config('APP_KEY')


# Create a function that makes a request to the Edamam API with the required ingredient as
# part of the search query (also included your Application ID and Application Key
def recipe_search(search_term):
    """
    :Purpose: Search for recipes from the web via an API.
    :param search_term: string - input chosen by user for a recipe.
    :return: a list of recipe(s) that match the search term by user.

    Function that takes search term input by user as
    an argument and returns a list of recipe(s) that match the search term.
    """
    url = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'
                       .format(search_term, APP_ID, APP_KEY))

    data = url.json()
    # print(requests.get(url))
    # print(data['hits']['recipe']['label'])
    return data['hits']
