from turtle import *
import random

bunny = Turtle()
bunny.shape("arrow")
bunny.speed(0)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return f"#{r:02x}{g:02x}{b:02x}"

#the commands
def draw_spiral(size_of_graph):
    for i in range (360//size_of_graph):
        bunny.color(random_color())
        currnent_heading = bunny.heading() 
        bunny.setheading(currnent_heading + size_of_graph)
        bunny.circle(100)


draw_spiral(5)







screen = Screen()
screen.exitonclick()