import turtle
from turtle import Turtle

X_POS = 350
Y_POS = 0


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_ycor = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_ycor)

    def go_down(self):
        new_ycor = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_ycor)
