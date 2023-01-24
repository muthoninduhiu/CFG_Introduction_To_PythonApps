import requests
from user_input import ingredient
from user_input import user_input
from user_input import read_text
import pprint
from decouple import config

APP_ID = config('APP_ID2')
APP_KEY = config('APP_KEY2')


# Cross-reference the ingredient against the Edamam nutrition analysis API


def comparison_check():
    """
        :Purpose: Search for recipes from the web via an API.
        :param : no parameters
        :return: a list of recipe(s) that match the search term by user.

        Function that takes search term input by user as
        an argument and returns a list of recipe(s) that match the search term.
        """
    url = requests.get('https://api.edamam.com/api/nutrition-data?app_id={}&app_key={}&ingr={}'
                       .format(APP_ID, APP_KEY, ingredient))

    data = url.json()
    print("Cross reference ingredient nutrition analysis api result:")
    pprint.pprint(data)

    # print(requests.get(url))
    # print(data['hits']['recipe']['label'])


user_input()
read_text()
comparison_check()
