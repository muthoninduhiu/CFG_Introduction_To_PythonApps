"""
Q1. Create a program that tells you whether or not you need an umbrella when you leave the house.
The program should:
1. Ask you if it is raining using input()
2. If the input is 'y', it should output 'Take an umbrella'
3. If the input is 'n', it should output 'You don't need an umbrella'
"""
is_raining = input('is it raining?(y/n)')
if is_raining == 'y':
    print("Take an umbrella")
else:
    print("You dont need an umbrella")

"""
Q2.I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit. I've
written a program to check that I can afford the cost, but something doesn't seem right.
Have a look at my program and work out what I've done wrong
my_money = input('How much money do you have? ')
boat cost = 20 + 5
if my_money < boat_cost:
print('You can afford the boat hire')
else:
print('You cannot afford the board hire')
"""
my_money = input('How much money do you have? ')
boat_cost = 20 + 5
if int(my_money) >= boat_cost:
    print('You cannot afford the boat hire')
else:
    print('You can afford the boat hire')

"""
Q3.Your friend works for an antique book shop that sells books between 1800 and 1950 and wants to
quickly categorise books by the century and decade that they were written.
Write a program that takes a year (e.g. 1872) and outputs the century and decade (e.g. "Nineteenth
Century, Seventies")
"""

which_century = input("Which Year is the Book from?")
check_century = int(which_century)
if 1800 < check_century < 1809:
    print("Early 19th Century")
elif 1810 < check_century < 1819:
    print("19th Century,tens")
elif 1820 < check_century < 1829:
    print("19th Century,twenties")
elif 1830 < check_century < 1839:
    print("19th Century,thirties")
elif 1840 < check_century < 1849:
    print("19th Century,forties")
elif 1850 < check_century < 1859:
    print("19th Century,fifties")
elif 1860 < check_century < 1869:
    print("19th Century,sixteens")
elif 1870 < check_century < 1879:
    print("19th Century,seventies")
elif 1880 < check_century < 1899:
    print("19th Century,eighties")
elif 1890 < check_century < 1899:
    print("19th Century,nineties")
elif 1900 < check_century < 1909:
    print("Early 20th Century")
elif 1910 < check_century < 1919:
    print("19th Century,tens")
elif 1920 < check_century < 1929:
    print("20th Century,twenties")
elif 1930 < check_century < 1939:
    print("20th Century,thirties")
elif 1940 < check_century < 1949:
    print("20th Century,forties")
elif 1950 < check_century < 1959:
    print("20th Century,fifties")
else:
    print("Not found")
