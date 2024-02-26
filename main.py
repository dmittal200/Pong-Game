from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800,height=500)
screen.tracer(0)

pad_l = Paddle((-370,0))
pad_r = Paddle((370,0))
ball = Ball()
Score = Scoreboard()

screen.listen()
screen.onkey(pad_r.up,"Up")
screen.onkey(pad_r.down, "Down")
screen.onkey(pad_l.up,"w")
screen.onkey(pad_l.down, "s")

game_on = True
while game_on:
    screen.update()
    sleep(ball.move_speed)
    ball.move()

    #detect upper wall collision
    if ball.ycor()>230 or ball.ycor()<-230:
        ball.bounce_y()

    # detect paddle collision
    if ball.distance(pad_r)<50 and ball.xcor()>330 or ball.distance(pad_l)<50 and ball.xcor()<-330:
        ball.bounce_x()

    #R paddle miss
    if ball.xcor()>370:
        ball.reset_position()
        Score.l_point()

    #L paddle miss
    if ball.xcor()<-370:
        ball.reset_position()
        Score.r_point()

screen.exitonclick()
