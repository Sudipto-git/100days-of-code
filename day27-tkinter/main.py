from tkinter import *
from turtle import RawTurtle, TurtleScreen

# Create the main window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Create a label
my_label = Label(window, text="I am a Label", font=("Arial", 24, "italic"))
my_label.grid(column=0, row=0)
my_label.config(text="New Text")
my_label.config(padx=50, pady=50)

# Create an entry
input_entry = Entry(window, width=10)
input_entry.grid(column=1, row=1)

# Define the button click function
def button_clicked():
    my_label.config(text=input_entry.get())

# Create a button
button = Button(window, text="dabau", command=button_clicked)
button.grid(column=1, row=0)
button = Button(window, text="aste chapo")
button.grid(column=2, row=1)

# Create a canvas for the turtle
canvas = Canvas(window, width=400, height=400)
canvas.grid(column=0, row=2, columnspan=3)

# # Create a TurtleScreen object
# turtle_screen = TurtleScreen(canvas)

# # Create a RawTurtle object
# tim = RawTurtle(turtle_screen)
# tim.shape("turtle")
# tim.write("Hello", font=("Arial", 24, "italic"))

# Start the tkinter main loop
window.mainloop()