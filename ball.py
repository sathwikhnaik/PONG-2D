from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.penup()
        self.goto(0, 0)
        self.mx = 10
        self.my = 10
        self.move_speed = 0.1

    def move(self):
        nx = self.xcor() + self.mx
        ny = self.ycor() + self.my
        self.goto(nx, ny)

    def bounce_y(self):
        self.my *= -1

    def bounce_x(self):
        self.mx *= -1
        self.move_speed *= 0.9

    def refresh(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

