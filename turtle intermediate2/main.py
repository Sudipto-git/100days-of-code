from turtle import *
from snake import Snake
import time
from food import food
from scorebord import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #used for realtime update of the screen

snake = Snake()
food = food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


  
 
game_on = True
while game_on :
    screen.update()
    time.sleep(0.1)# make the snake move slower
    #realtime update for the screen to make it look like the snake is moving
    
    snake.move()
    
    #adetect collision with food
    if snake.head.distance(food) <15:
        food.refresh()

        

    





screen.exitonclick()