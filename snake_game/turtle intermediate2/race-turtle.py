from turtle import *
import random


is_race_on = False

#screen setup
screen = Screen()
screen.setup(width = 500, height = 500)
screen.bgcolor("black")
user_bet = screen.textinput(title = "make your bet", prompt = "which turtle will win the race? Enter a color : ")   
print(user_bet)
color = ["red", "blue", "green", "yellow", "purple", "orange"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_position[turtle_index])
    all_turtles.append(new_turtle)
    

        
          
if user_bet :
    is_race_on = True
    
while is_race_on:
    
    for new_turtle in all_turtles: 
        
        if new_turtle.xcor()>230:
            is_race_on = False
            
            winning_color = new_turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won! The {winning_color} turtle is the winner")
            else:
                print(f"you have lost! The {winning_color} turtle is the winner")
            
            
        random_distance = random.randint(0,10)
        new_turtle.forward(random_distance)






screen.exitonclick()