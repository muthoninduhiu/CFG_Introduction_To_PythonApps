"""
Question 2
I'm setting up my own market stall to sell chocolates.
I need a basic till to check the prices of
different chocolates that I sell.
I've started the program and included the chocolates and their prices.
Finish the program by asking
the user to input an item and then output its price.
"""
chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}
which_chocolate = input("Which chocolate would you prefer?(white,milk,dark,vegan)?")
if which_chocolate == "white":
    print("Price: {}".format(chocolates['white']))
elif which_chocolate == "milk":
    print("Price: {}".format(chocolates['milk']))
elif which_chocolate == "dark":
    print("Price: {}".format(chocolates['dark']))
elif which_chocolate == "vegan":
    print("Price: {}".format(chocolates['vegan']))
else:
    print("Unfortunately we dont have that yet")
