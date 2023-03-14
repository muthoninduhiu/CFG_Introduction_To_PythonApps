from recipe_search import recipe_search

print('Welcome to Recipe Search!\n'
      'We\'ll choose a couple of recipes based on an ingredient of your choice')

ingredient = input('Enter an ingredient: ')


# Get the returned recipes from the API response
def user_input():
    """
        :Purpose: Get user input and use it to pull data from the API
        :return: has no return type
        Function that asks for user  input and uses that to search for the value in the API
        then save the results to a file
        """
    list_of_recipes = recipe_search(ingredient)
    if not list_of_recipes:
        print("No recipe matches your search!")
    else:
        for result in list_of_recipes:
            recipes = result['recipe']
            # print(recipes)

            # order results for some parameter : totalWeight,calories,total_time,yield
            recipe_weight = []
            for weight in list_of_recipes:
                recipe_weight.append(weight['recipe']['totalWeight'])
                # print(recipe_weight)
                print(weight['recipe']['label']+": ")
                print(sorted(recipe_weight))

            recipe_calories = []
            for calories in list_of_recipes:
                recipe_calories.append(calories['recipe']['calories'])
                # print(sorted(recipe_calories))

            recipe_total_time = []
            for time in list_of_recipes:
                recipe_total_time.append(time['recipe']['totalTime'])
                # print(sorted(recipe_total_time))



