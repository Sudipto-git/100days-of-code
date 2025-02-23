from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip  # this is for copying the password to the clipboard
import json  # this is for saving the data in a json file

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    user_name = User_name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Warning", message="Please don't leave any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:

            data.update(new_data)

            with open("data.json", "w") as data_file:
            # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)
            User_name_entry.delete(0, END)
            
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_files:
            data = json.load(data_files)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website, message = f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, bg="white")
img = PhotoImage(file="/Users/sudipto/Documents/code/projects/100days of code/day 29 password manager/logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
User_name_label = Label(text="Username:")
User_name_label.grid(row=2, column=0)
email_label = Label(text="Email:")
email_label.grid(row=3, column=0)
password_label = Label(text="Password:")
password_label.grid(row=4, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()
User_name_entry = Entry(width=35)
User_name_entry.grid(row=2, column=1)
email_entry = Entry(width=35)
email_entry.grid(row=3, column=1)
password_entry = Entry(width=35)
password_entry.grid(row=4, column=1)

# Buttons
search_button = Button(text="Search", width=14, command = find_password )
search_button.grid(row=1, column=2)

Generate_password_button = Button(text="Generate Password", command=generate_password)
Generate_password_button.grid(row=4, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()