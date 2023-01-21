from turtle import Turtle, Screen

class Paddle(Turtle):

    def __init__(self , position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        y_position = self.ycor() + 20
        self.goto(self.xcor(), y_position)

    def down(self):
        y_position = self.ycor() - 20
        self.goto(self.xcor(), y_position)
