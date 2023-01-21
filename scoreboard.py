from turtle import Turtle

class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.updade_score()


    def updade_score(self):
        self.clear()
        self.goto(-120, 200)
        self.write(f"Score : {self.left_score}", align="center", font=("Comic Sans", 30, "normal"))
        self.goto(120, 200)
        self.write(f"Score : {self.right_score}", align="center", font=("Comic Sans", 30, "normal"))

    def left_point(self):
        self.left_score += 1
        self.updade_score()

    def right_point(self):
        self.right_score += 1
        self.updade_score()

