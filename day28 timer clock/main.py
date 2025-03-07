from tkinter import *
import math

# Constants
YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
PINK = "#e2979c"
RED = "#e7305b"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0
    start_button.config(state=NORMAL)
    reset_button.config(state=DISABLED)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    start_button.config(state=DISABLED)
    reset_button.config(state=NORMAL)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)
        
# ---------------------------- SNAP ------------------------------- #
def snap_time():
    current_time = Canvas.itemcget(timer_text, "text")
    snap_label = Label(text = f"snap time = {current_time}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()   
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="/Users/sudipto/Documents/code/projects/100days of code/day28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, bg=PINK, fg=GREEN, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, bg=PINK, fg=RED, highlightthickness=0, state=DISABLED)
reset_button.grid(column=2, row=2)

snap_button = Button(text="Snap", command= snap_time, bg=PINK, fg=RED, highlightthickness=0)
snap_button.grid(column=1, row=2)

snap_label = Label(text="", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 20, "bold"))
snap_label.grid(column=1, row=3)


check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()