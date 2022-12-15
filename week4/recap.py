"""
Q1.What brackets are used to create a list? []
What brackets are used to create dictionaries? {}
"""
"""
Question 2: What is the result of this program? list index out of range
"""
cheeses = [
    'brie',
    'cheddar',
    'wensleydale',
    'edam',
]
print(cheeses[3])
"""
Question 3: This program raises an error when I run it.
 What do I need to change to get it to run? add square bracket 
 to complete list of dictionaries
"""
trees = [
    {'leaf_colour': 'green', 'height': 2120},
    {'leaf_colour': 'green', 'height': 2300},
]
new_tree = {
    'leaf_colour': 'green',
    'height': 1020
}
trees.append(new_tree)
print(trees)
