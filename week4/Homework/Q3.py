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
import random

ticket1_lottery = random.sample(range(1, 70), k=7)
ticket2_lottery = random.sample(range(1, 70), k=7)

t1 = sorted(ticket1_lottery)
t2 = sorted(ticket2_lottery)

print('Lottery ticket #1 {}'.format(t1))
print('Lottery ticket #2 {}'.format(t2))

points = 0
for number in t2:
   if number in t1:
       points += 1
"""
if (points < 3):
   print('None, try again.'.format(points))
if (points == 3):
   print('£20')
if (points == 4):
   print('£40')
if (points == 5):
   print('£100')
if (points == 6):
   print('£10,000')
if (points == 7):
   print('£1,000,000')"""