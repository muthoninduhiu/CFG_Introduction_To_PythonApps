from recipe_search import recipe_search
# Ask the user to enter an ingredient that they want to search for
ingredient = input('Enter an ingredient: ')


# Get the returned recipes from the API response
def user_input():
    """
        :Purpose: Get user input and use it to pull data from the API
        :return: has no return type
        Function that asks for user  input and uses that to search an API
        """
    list_of_recipes = recipe_search(ingredient)

    if not list_of_recipes:
        print("No recipe matches your search!")
    else:
        for result in list_of_recipes:
            recipes = result['recipe']
            # print(recipes)
            # Save the results to a file recipe_names.txt
            with open('recipe_names.txt', 'a+') as recipe_details:
                recipe_details.write("Name: {}\nThe Ingredients: {}\nWeight: {}\nCuisine Type: {}\nHealth Label: {}\n"
                                     .format(recipes['label'],
                                             (recipes['ingredientLines']),
                                             (recipes['totalWeight']),
                                             recipes['cuisineType'],
                                             recipes['healthLabels']))
                recipe_details.write("\n")


# Display the recipes for each search result
def read_text():
    with open('recipe_names.txt', 'r') as text_file:
        contents = text_file.read()
        print(contents)
