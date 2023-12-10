from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager App")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

web_name_label = Label(text="Website: ")
web_name_label.grid(row=1, column=0)

web_name_entry = Entry(width=38)
web_name_entry.grid(row=1, column=1, columnspan=2)
web_name_entry.focus()

user_name_label = Label(text="Username/ Email: ")
user_name_label.grid(row=2, column=0)

user_name_entry = Entry(width=38)
user_name_entry.grid(row=2, column=1, columnspan=2)
user_name_entry.insert(0, "elwany_hassan@hotmail.com")

# Create a pseudo-row for password entry and generate button
password_frame = Frame(window)
password_frame.grid(row=3, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(password_frame, width=21)
password_entry.grid(row=0, column=1)

generate_pass = Button(password_frame, text="Generate Password")
generate_pass.grid(row=0, column=2)

add_button = Button(text="Add", width=38)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
