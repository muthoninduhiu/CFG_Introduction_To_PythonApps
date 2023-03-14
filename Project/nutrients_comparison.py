import requests
from user_input import ingredient
from user_input import user_input
from save_to_file import read_text, write_to_file
from diet_mealType import extra_parameters

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
    url = requests.get('https://api.edamam.com/api/nutrition-data',
                       headers={'Accept': 'application/json'},
                       params={
                           'app_id': APP_ID,
                           'app_key': APP_KEY,
                           'type': 'any',
                           'ingr': ingredient,
                       })

    data = url.json()
    print("Cross reference ingredient nutrition analysis api result:")
    pprint.pprint(data)

    # print(requests.get(url))
    # print(data['hits']['recipe']['label'])


extra_parameters()
user_input()
comparison_check()
save = input('Would you like to save your work to a file?(Yes/No)')
if save == 'yes':
    write_to_file()
read = input('Would you like to read your saved work?(Yes/No)')
if read == 'yes':
    read_text()
print('\nBye, thank you for searching with us!!!')
