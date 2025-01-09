from turtle import Screen
from PPaddle import Paddle
from ball import Ball
import time
from scorebord import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

r_Paddle = Paddle((350, 0))
l_Paddle = Paddle((-350, 0))
ball = Ball()
Scoreboard = Scoreboard()




def r_paddle_up():
    r_Paddle.up()

def r_paddle_down():
    r_Paddle.down()

def l_paddle_up():
    l_Paddle.up()

def l_paddle_down():
    l_Paddle.down()
    

screen.listen()
screen.onkey(r_paddle_up, "Up")
screen.onkey(r_paddle_down, "Down")
screen.onkey(l_paddle_up, "w")
screen.onkey(l_paddle_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.09)
    screen.update()
    ball.move()
    Scoreboard.update_scorebord()
    
    #detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    
    #detect collision with paddles
    if ball.distance(r_Paddle) < 50 and ball.xcor()>320 or ball.distance(l_Paddle) < 50 and ball.xcor()<-320: 
        
        ball.bounce_x()
    #detect R paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        Scoreboard.l_point()
        
    #detect L paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        Scoreboard.r_point()
        
screen.exitonclick()