
with open('people.txt', 'r') as text_file:
    contents = text_file.read()

print(contents)

with open('people.txt', 'w+') as text_file:
    people = 'Joanne \nSusan \nAmina'

    text_file.write(people)

customer_input = input("Enter new to do item: ")
with open('todo.txt', 'r') as text_file:
    contents = text_file.read()
    contents += customer_input + '\n'
with open('todo.txt', 'w+') as text_file:
    text_file.write(contents)
print("Your new to-tolist is:\n")
print(contents)
