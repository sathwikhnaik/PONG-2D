from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(width=800, height=600)
screen.tracer(0)

rpaddle = Paddle((350, 0))
rpaddle.color("Blue")
lpaddle = Paddle((-350, 0))
lpaddle.color("Red")
ball = Ball()
sc = ScoreBoard()

screen.listen()
screen.onkeypress(rpaddle.up, "Up")
screen.onkeypress(rpaddle.down, "Down")
screen.onkeypress(lpaddle.up, "w")
screen.onkeypress(lpaddle.down, "s")

game_is_on = True


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    screen.onkey(sc.t_off, "space")
    if sc.gg == 1:
        sc.win()
        break
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.refresh()
        sc.l_point()

    if ball.xcor() < -380:
        ball.refresh()
        sc.r_point()


screen.exitonclick()
