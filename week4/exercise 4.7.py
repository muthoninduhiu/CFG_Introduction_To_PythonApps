"""
Exercise 4.7: Write a program to create a random name. You should have a list of random firstnames
and a list of lastnames. Choose a random item from each and display the result.
Extension: Using list of verbs and a list of nouns, create randomised sentences
"""
import random

first_names = [
    "mary", "anne", "nduhiu", "ashley", "nimmo"
]

last_names = [
    "muthoni", "betty", "wachira", "carol", "wanja"
]
first_name = random.choice(first_names)
last_name = random.choice(last_names)

print("{} {}".format(first_name, last_name))
