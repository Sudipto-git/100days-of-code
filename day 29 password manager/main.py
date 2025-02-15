from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip #this is for copying the password to the clipboard
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','@','#','$','%','^','&','*','(',')','_','+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)




    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    website = website_entry.get()
    user_name = User_name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Warning", message="Please don't leave any field empty")
        
    else:
        is_ok = messagebox.askokcancel(title="website", message=f"These are the details entered: \nWebsite: {website} \nUser Name: {user_name} \nEmail: {email} \nPassword: {password}   \nIs it correct?")
        #this is for the pop up window
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} || {user_name} || {email} || {password}\n\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                email_entry.delete(0, END)
                User_name_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


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
website_entry.focus()
User_name_entry = Entry(width = 35)
User_name_entry.grid(row = 2,column = 1)
email_entry = Entry(width = 35)
email_entry.grid(row = 3,column=1)
password_entry = Entry(width = 35)
password_entry.grid(row = 4,column = 1)


# buttons
Generate_password_button = Button(text = "Generate Password",command= generate_password)
Generate_password_button.grid(row = 4,column= 2)

add_button = Button(text = "Add",width=36,command= save)
add_button.grid(row = 5,column= 1, columnspan = 2)

window.mainloop()



window.mainloop()