from tkinter import *
import random
import os
import pandas as pd

try:
    data = pd.read_csv("/Users/sudipto/Documents/code/projects/100days of code/day31_flas_card_app/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("/Users/sudipto/Documents/code/projects/100days of code/day31_flas_card_app/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card["French"])
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    flip_timer=window.after(3000, func = flip_card)
    
def flip_card():
    canvas.itemconfig(title_text, text="English",fill = "green")
    canvas.itemconfig(word_text, text=current_card["English"], fill="green")
    canvas.itemconfig(card_background, image=card_back_img)
    
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("/Users/sudipto/Documents/code/projects/100days of code/day31_flas_card_app/words_to_learn.csv", index=False)
    next_card()
    
# ------------------------ UI SETUP --------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg="#B1DDC6")
flip_timer = window.after(3000, func = flip_card)

canvas = Canvas(width=800, height=526, bg="#B1DDC6", highlightthickness=0)

card_back_img = PhotoImage(file="/Users/sudipto/Documents/code/projects/100days of code/day31_flas_card_app/card_back.png")
card_front_img = PhotoImage(file="/Users/sudipto/Documents/code/projects/100days of code/day31_flas_card_app/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"),fill="black")
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"),fill="black")
canvas.grid(row=0, column=0, columnspan=2)


# ------------------------ BUTTONS --------------------------------- #
cross_image = PhotoImage(file="/Users/sudipto/Documents/code/projects/100days of code/day31_flas_card_app/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

right_image = PhotoImage(file="/Users/sudipto/Documents/code/projects/100days of code/day31_flas_card_app/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)


next_card()
window.mainloop()