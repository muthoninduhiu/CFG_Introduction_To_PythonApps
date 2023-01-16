import requests


def recipe_search(search_term):
    """
    :Purpose: Search for recipes from the web via an API.
    :param search_term: string - input chosen by user for a recipe.
    :return: a list of recipe(s) that match the search term by user.

    Function that takes search term input by user as
    an argument and returns a list of recipe(s) that match the search term.
    """
    app_id = "2e66588b"
    app_key = "94e8f7bfbc31d8515e397b83f366d84a"
    url = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'
                       .format(search_term, app_id, app_key))

    data = url.json()
    # print(requests.get(url))
    # print(data['hits']['recipe']['label'])
    return data['hits']


def user_input():
    """
        :Purpose: Get user input and use it to pull data from the API
        :return: no return value.

        Function that asks for user  input and uses that to search an API
        """
    ingredient = input('Enter an ingredient: ')
    search_results = recipe_search(ingredient)
    for result in search_results:
        recipes = result['recipe']
        # print(recipes['label'])
        # print(recipe['label'])
        """
            I need this to be a method on its own so that each function has one purpose
            anyone with an idea how i can go about that or it stays this way?
        """
        with open('recipe_names.txt', 'a+') as recipe_details:
            recipe_details.write("Name: {}\nThe Ingredients: {}\nWeight: {}\nCuisine Type: {}\n"
                                 .format(recipes['label'],
                                         recipes['ingredientLines'],
                                         recipes['totalWeight'],
                                         recipes['cuisineType']))
            recipe_details.write("\n")


user_input()


def read_text():
    with open('recipe_names.txt', 'r') as text_file:
        contents = text_file.read()
        print(contents)


