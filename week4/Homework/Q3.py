"""
Question 3

Write a program that simulates a lottery. The program should have a list of
seven numbers that represent a lottery ticket. It should then
generate seven random numbers. After comparing the two
sets of numbers, the program should output a prize based on the number of matches:
● £20 for three matching numbers
● £40 for four matching numbers
● £100 for five matching numbers
● £10000 for six matching numbers
● £1000000 for seven matching numbers
"""
import random


# create empty list to hold randomly generated tickets
def ticket_making():
    random_numbers = []
    for number in range(1, 8):
        number = random.randint(0, 9)
        random_numbers.append(number)

    return random_numbers


print(ticket_making())

print(ticket_making())
