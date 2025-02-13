from tkinter import *
from PIL import Image, ImageTk


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)


# Load the background image
background_image = PhotoImage(file="/Users/sudipto/Documents/code/projects/100days of code/day27-tkinter/image copy.png")
background_image = background_image.resize((300, 100), Image.ANTIALIAS)
background_photo = ImageTk.PhotoImage(background_image)



# Create a canvas and set the background image
canvas = Canvas(window, width=300, height=100,bg = "white") 
canvas.grid(column=0, row=0, columnspan=3, rowspan=3)
canvas.create_image(0, 0, anchor=NW, image=background_image)
canvas.pack()


miles_input = Entry(window, width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(window, text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(window, text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(window, text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(window,text = "km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(window, text="Calculate", command = miles_to_km)
calculate_button.grid(column=1, row=2)

def on_button_click(event):
    miles_to_km()

button_text = canvas.create_text(150, 80, text="Calculate", font=("Arial", 16, "bold"), fill="white")
canvas.tag_bind(button_text, "<Button-1>", on_button_click)



window.mainloop()