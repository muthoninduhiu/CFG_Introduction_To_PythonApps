from recipe_search import recipe_search
from user_input import ingredient


def write_to_file():
    text = recipe_search(ingredient)
    for result in text:
        my_recipe_text = result['recipe']
        # Save the results to a file recipe_names.txt

        with open('recipe_names.txt', 'a+', encoding='utf-8') as recipe_details:
            recipe_details.write("Name: {}\nThe Ingredients: {}\nWeight: {}\nCuisine Type: {}\nHealth Label: {}\n"
                                 .format(my_recipe_text['label'],
                                         (my_recipe_text['ingredientLines']),
                                         (my_recipe_text['totalWeight']),
                                         my_recipe_text['cuisineType'],
                                         my_recipe_text['healthLabels']))
            recipe_details.write("\n")


# Display the recipes for each search result
def read_text():
    """
            :Purpose: Read data in the text file and display it
            :return: has no return type
            """
    with open('recipe_names.txt', 'r', encoding='utf-8') as text_file:
        contents = text_file.read()
        print(contents)
