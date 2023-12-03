from tkinter import *

root = Tk()


#creating a Label widget 
my_label1 = Label(root, text="Hello World!")
my_label2 = Label(root, text="My Name is Hassan Elwany")

#put the text label onto screen
my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=0)

root.mainloop()