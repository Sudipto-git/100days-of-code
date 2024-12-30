# import colorgram

# rgb_colors = []
# colors = colorgram.extract('/Users/sudipto/Documents/code/projects/100days of code/turtle-intermediate/aparajita.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.r
#     b = color.rgb.r
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)
#the color list of aparajita
# [(178, 178, 178), (225, 225, 225), (30, 30, 30), (55, 55, 55), (134, 134, 134), (211, 211, 211), (20, 20, 20), (82, 82, 82), (80, 80, 80), (92, 92, 92), (156, 156, 156), (195, 195, 195), (158, 158, 158), (160, 160, 160), (51, 51, 51), (140, 140, 140), (74, 74, 74), (81, 81, 81), (227, 227, 227), (69, 69, 69), (114, 114, 114), (63, 63, 63), (187, 187, 187), (112, 112, 112), (57, 57, 57), (254, 254, 254), (59, 59, 59), (210, 210, 210), (186, 186, 186), (185, 185, 185)]
 
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
color_list = [(178, 178, 178), (225, 225, 225), (30, 30, 30), (55, 55, 55), (134, 134, 134), (211, 211, 211), (20, 20, 20), (82, 82, 82), (80, 80, 80), (92, 92, 92), (156, 156, 156), (195, 195, 195), (158, 158, 158), (160, 160, 160), (51, 51, 51), (140, 140, 140), (74, 74, 74), (81, 81, 81), (227, 227, 227), (69, 69, 69), (114, 114, 114), (63, 63, 63), (187, 187, 187), (112, 112, 112), (57, 57, 57), (254, 254, 254), (59, 59, 59), (210, 210, 210), (186, 186, 186), (185, 185, 185)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")

numberOfDots = 500


for dot_counts in range(1, numberOfDots + 1):
    tim.dot(10, random.choice(color_list))
    tim.forward(20)

    if dot_counts % 10 == 0:
        
        tim.setheading(90)
        tim.forward(5)
        tim.setheading(180)
        tim.forward(200)
        screen = t.Screen()
        tim.setheading(0)  

screen.exitonclick()

 

    