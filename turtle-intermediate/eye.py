# import colorgram

# rgb_colors = []
# colors = colorgram.extract('/Users/sudipto/Documents/code/projects/100days of code/turtle-intermediate/short.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.r
#     b = color.rgb.r
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)

# [(196, 196, 196), (137, 137, 137), (53, 53, 53), (225, 225, 225), (32, 32, 32), (162, 162, 162), (81, 81, 81), (163, 163, 163), (39, 39, 39), (228, 228, 228), (81, 81, 81), (59, 59, 59), (75, 75, 75), (88, 88, 88), (75, 75, 75), (42, 42, 42)]

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
color_list = [(196, 196, 196), (137, 137, 137), (53, 53, 53), (225, 225, 225), (32, 32, 32), (162, 162, 162), (81, 81, 81), (163, 163, 163), (39, 39, 39), (228, 228, 228), (81, 81, 81), (59, 59, 59), (75, 75, 75), (88, 88, 88), (75, 75, 75), (42, 42, 42)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed(0)

numberOfDots = 500000


for dot_counts in range(1, numberOfDots + 1):
    tim.dot(10, random.choice(color_list))
    tim.forward(20)

    if dot_counts % 10 == 0:
        
        tim.setheading(90)
        tim.forward(2)
        tim.setheading(180)
        tim.forward(200)
        screen = t.Screen()
        tim.setheading(0)  

screen.exitonclick()
