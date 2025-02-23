from tkinter import *
from random import *
import os

# ------------------------ UI SETUP --------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg="#B1DDC6")

canvas = Canvas(width=800, height=526, bg="#B1DDC6", highlightthickness=0)

card_back_img = PhotoImage(file="/Users/sudipto/Documents/code/projects/100days of code/day31_flas_card_app/card_back.png")
card_front_img = PhotoImage(file="/Users/sudipto/Documents/code/projects/100days of code/day31_flas_card_app/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"),fill="black")
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"),fill="black")
canvas.grid(row=0, column=0, columnspan=2)


# ------------------------ BUTTONS --------------------------------- #
cross_image = PhotoImage(file="/Users/sudipto/Documents/code/projects/100days of code/day31_flas_card_app/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=lambda: canvas.itemconfig(card_background, image=card_back_img))
cross_button.grid(row=1, column=0)

right_image = PhotoImage(file="/Users/sudipto/Documents/code/projects/100days of code/day31_flas_card_app/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=lambda: canvas.itemconfig(card_background, image=card_front_img))
right_button.grid(row=1, column=1)



window.mainloop()