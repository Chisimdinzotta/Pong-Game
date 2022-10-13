from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

right_paddle = Paddle(380,0)
left_paddle = Paddle(-380,0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.up, "q")
screen.onkey(left_paddle.down, "a")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

#Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

#Detect collsion with paddle
    if ball.distance(right_paddle) < 40 and ball.xcor() > 350 or ball.distance(left_paddle) < 40 and ball.xcor() < -350:
        #The 320 checks when it has moved past the first layer of topper most part of the paddle
        ball.bounce_x()

#Detect if right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()
#As you know in line 13 the paddle is at 350 and is 20 pixle thick

#Detect if left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
