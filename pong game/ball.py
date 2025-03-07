from turtle import *

class Ball(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 4
        self.shape("circle")
        self.size = 0.5
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y) 
        
    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1 
        self.move_speed *= 2

    
        
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()