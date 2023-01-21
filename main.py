import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

game_start = True



screen.listen()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

while game_start:
    time.sleep(ball.boll_speed)
    screen.update()
    ball.move()

    #  Collision wall

    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.balance()

    # Collision right/left side

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) <50 and ball.xcor() < -320:
        ball.balance_x()

    # Misses paddle right site

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.left_point()

    # Misses paddle left  site

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.right_point()

screen.exitonclick()
