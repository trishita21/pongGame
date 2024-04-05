from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(paddle1.go_up,"Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up,"w")
screen.onkey(paddle2.go_down,"s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320:
        print("Collision with R Paddle")
        ball.bounce_x()

    # Detect collision with left paddle
    if ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect out of bounds
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset()
        score.r_point()





screen.exitonclick()