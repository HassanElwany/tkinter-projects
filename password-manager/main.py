from tkinter import *
from tkinter import messagebox
import random, string
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    # Define character sets for letters, symbols, and numbers
    letters = string.ascii_letters  # includes both uppercase and lowercase letters
    symbols = string.punctuation   # includes various punctuation symbols
    numbers = string.digits         # includes digits 0-9

    # Generate random counts for letters, symbols, and numbers
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    #Use list comprehensions to generate lists of random choices
    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]

    #concatenate lists of random choices to pass list
    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)


    #print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button():
    website_name = web_name_entry.get()
    user_name_value = user_name_entry.get()
    password_value = password_entry.get()

    if len(website_name) == 0 or len(password_value) == 0:
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")
    
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"here your info you entered: \nEmail: {user_name_value}\nPassword: {password_value}\nIs it ok to save your password?")

        if is_ok:

            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_name} | {user_name_value} | {password_value}\n")

            web_name_entry.delete(0, END)
            password_entry.delete(0, END)
            print(f"{website_name} | {user_name_value} | {password_value}")


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


generate_pass = Button(password_frame, text="Generate Password", command=generate_password)
generate_pass.grid(row=0, column=2)

add_button = Button(text="Add", width=38, command=add_button)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
