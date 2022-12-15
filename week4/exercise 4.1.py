"""
When I'm travelling in the winter I often forget to pack warm clothes. Let's write a
program to help me to remember the right clothes.
The program should check if the first item in the clothes list is "shorts" .
If it is it should change the value to "warm coat" .

Change the other items in the list to clothing more appropriate to winter if the first
item is shorts
"""
clothes = [
    "shorts",
    "shoes",
    "t-shirt"
]
if clothes[0] == "shorts":
    clothes[0] = "warm coat"
    clothes[1] = "boots"
    clothes[2] = "scarf"
print(clothes)
print(len(clothes))
print(max(clothes))
print(min(clothes))
print(sorted(clothes))
print(list(reversed(clothes)))
