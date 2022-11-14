import turtle
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.hideturtle()
        self.goto(position)
        self.showturtle()

    def up(self):
        ny = self.ycor() + 20
        self.sety(ny)

    def down(self):
        ny = self.ycor() - 20
        self.sety(ny)
