from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        with open("/Users/sudipto/Documents/code/projects/100days of code/snake_game/turtle intermediate2/data.txt") as data:
            self.high_score = int(data.read())
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()  # Corrected method call
        
    def reset(self):
        if self.score >self.high_score:
            self.high_score = self.score
            with open("/Users/sudipto/Documents/code/projects/100days of code/snake_game/turtle intermediate2/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= "right", font=FONT)