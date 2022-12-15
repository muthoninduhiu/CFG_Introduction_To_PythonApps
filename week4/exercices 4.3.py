"""
Exercise 4.3: Whenever I'm shopping and I buy some bread I always forget to buy butter.
Create a list and if 'bread' is in the list, add 'butter' to the shopping list.
Try running the program with and without bread in the list to check that your program works.
Remember the in operator checks if an item is in a list and the .append() method adds an item to a
list.
"""
shopping_list = [
     "bread", "sugar", "soy sauce", "salt", "vinegar", "flour"
]
if "bread" in shopping_list:
    shopping_list.append("butter")

print(shopping_list)
