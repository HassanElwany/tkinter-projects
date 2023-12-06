from tkinter import *
from tkinter import ttk
window = Tk()
window.minsize(width=700, height=500)

window.title("First GUI app")

my_label = Label(text="I am a label", font=("Arial", 24))
my_label.pack()


my_label.config(text="My name is Hassan")


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)



button = Button(text="Click here", command=button_clicked).pack()



input = Entry(width=75).pack()








window.mainloop()