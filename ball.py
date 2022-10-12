from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        #self.shapesize(1)
        self.goto(0,0)
        self.penup()
        self.x_move = 10
        self.y_move = 10




    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_xcor)

    def bounce(self):
       self.x_move *= -1
       self.y_move *= -1




