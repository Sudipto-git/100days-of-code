import tkinter as tk
import turtle as tim

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tk.Label(text="I am a Label", font=("Arial", 24,"italic"))
my_label.pack(side = "left")


tim.shape("turtle")
tim.write("Hello", font=("Arial", 24, "italic"))

turtle_screen = tim.Screen(window)




window.mainloop()


