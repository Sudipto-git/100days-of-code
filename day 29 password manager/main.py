# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    website = website_entry.get()
    user_name = User_name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    
    with open("data.txt","a") as data_file:
         data_file.write(f"{website} || {user_name} || {email} || {password}\n")
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200,bg = "white")
img = PhotoImage(file="/Users/sudipto/Documents/code/projects/100days of code/day 29 password manager/logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)
# if use grid u cant use pack

# Labels
website_label = Label(text = "Website:")
website_label.grid(row = 1,column = 0)
User_name_labell = Label(text = "Username:")
User_name_labell.grid(row = 2,column = 0)
email_label = Label(text ="Email: ")
email_label.grid(row = 3,column = 0)
password_label = Label(text ="Password: ")
password_label.grid(row = 4,column = 0)

# Entries
website_entry = Entry(width = 35)
website_entry.grid(row = 1,column = 1)
User_name_entry = Entry(width = 35)
User_name_entry.grid(row = 2,column = 1)
email_entry = Entry(width = 35)
email_entry.grid(row = 3,column=1)
password_entry = Entry(width = 35)
password_entry.grid(row = 4,column = 1)

# buttons
Generate_password_button = Button(text = "Generate Password")
Generate_password_button.grid(row = 4,column= 2)

add_button = Button(text = "Add",width=36,command= save)
add_button.grid(row = 5,column= 1, columnspan = 2)

window.mainloop()



window.mainloop()