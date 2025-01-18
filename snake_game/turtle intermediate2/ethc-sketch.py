from turtle import *


tu = Turtle()
tutu = Turtle()
screen = Screen()

def move_forward():
    tu.forward(10)
def move_backward():
    tu.backward(10)
def turn_left():
    tu.left(10)
def turn_right():
    tu.right(10)
def counter_clockwise():
    tu.circle(100)
def clockwise():
    tu.circle(-100)
    
def clear():
    tu.clear()
    tu.penup()
    tu.home()
    tu.pendown()

screen.listen()
screen.onkey(key = "w" ,fun = move_forward)
screen.onkey(key = "s" ,fun = move_backward)
screen.onkey(key = "a" ,fun = turn_left)
screen.onkey(key = "d" ,fun = turn_right)
screen.onkey(key = "q", fun = counter_clockwise)
screen.onkey(key = "e", fun = clockwise)
screen.onkey(key = "c", fun = clear)

screen.exitonclick()

#higher order function is used here. The function move_forward is passed as an argument to the onkey function. This is an example of higher order function.