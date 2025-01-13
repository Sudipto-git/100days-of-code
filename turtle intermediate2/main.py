from turtle import *
from snake import Snake
import time
from food import food
from score import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #used for realtime update of the screen

snake = Snake()
food = food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


  
game_on = True
while game_on :
    screen.update()
    time.sleep(0.1)# make the snake move slower
    #realtime update for the screen to make it look like the snake is moving
    
    snake.move()
    
    #adetect collision with food
    if snake.head.distance(food) <15:
        print("Yum")
        food.refresh()
        snake.extend()
        scoreboard.update_scoreboard()
        scoreboard.increase_score()
        
        
    #snake head collision with wall
    
    if snake.head.xcor() > 290 or snake.head.xcor()< -290 or snake.head.ycor() > 290 or snake.head.ycor () < -290:
        game_on = False
        scoreboard.game_over()

    #detect collision with tail
    #if head collide with any segment with taile then the game will be over
    #trigger game_over
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_on = False
            scoreboard.game_over()
            
        

    





screen.exitonclick()