from turtle import Turtle,Screen
from create_paddle import Paddle
from create_ball import Ball
import time
from score_board import Scoreboard
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("pong")
screen.tracer(0)



r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

ball=Ball()
score=Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


is_game_on=True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(r_paddle)<30 and ball.xcor()>320 or ball.distance(l_paddle)<30 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.xcor()>380 :
        ball.reset_position()
        screen.update()
        score.l_point()


    if ball.xcor()<-380:
        ball.reset_position()
        screen.update()
        score.r_point()

screen.exitonclick()