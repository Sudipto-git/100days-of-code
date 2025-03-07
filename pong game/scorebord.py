from turtle import *

class Scoreboard(Turtle):
    
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        
        self.color("red")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        
        self.update_scorebord()
        
    def update_scorebord(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align="center", font=("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(self.r_score,align="center", font=("Courier", 80, "normal"))
        
        
    def l_point(self):
        self.l_score += 1
        self.update_scorebord()
        
    def r_point(self):
        self.r_score +=1
        self.update_scorebord()
        