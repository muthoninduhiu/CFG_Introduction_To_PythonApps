from tkinter import *

root = Tk()
root.title("Recipe Search")
heading = Frame(root)
frame = Frame(root)
result = Frame(root)

Label(heading,
      text="Recipe Search",
      pady=20,
      font=('Times', 30, 'bold')).pack(side=TOP)

Label(
    frame,
    text='Search Here: '
).pack(side=LEFT)

Label(result, 
  text = 'Search results:',
  pady = 1,
  font = ('Times', 17)).pack(side = LEFT)

input_box = Entry(frame, width = 50)
input_box.pack(side =  LEFT, fill = BOTH, expand = 5)
input_box.focus_set()

query = ''
text = Text(root, font = ('Times',13), padx = 55, pady = 10)


root.mainloop()