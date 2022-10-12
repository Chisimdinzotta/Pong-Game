from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")


right_paddle = Paddle(-350,0)
left_paddle = Paddle(350,0)
ball = Ball()


screen.listen()

screen.onkey(left_paddle.up, "Up")
screen.onkey(left_paddle.down, "Down")

screen.onkey(right_paddle.up, "q")
screen.onkey(right_paddle.down, "a")

game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(0.01)

    if ball.ycor() > 280 or ball.xcor() < -280:
        ball.bounce()



screen.exitonclick()
