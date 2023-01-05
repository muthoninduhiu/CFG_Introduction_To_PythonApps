"""
Question 2
This program should save my data to a file, but it doesn't work when I run it. What is the problem
and how do I fix it?

poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'r') as poem_file:
poem_file.write(poem)

we have not created poem.txt

w+
"""


with open('poem.txt', 'w+') as poem_file:
    poem = 'I like Python and I am not very good at poems'
    poem_file.write(poem)
