import turtle
import paddle
import time
from scoreboard import Scoreboard
from ball import Ball

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title('Pingpong Game')
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

ball = Ball()
pad1 = paddle.Paddles((-370, 0))
pad2 = paddle.Paddles((370, 0))
score_pad1 = Scoreboard((-300, 260))
score_pad2 = Scoreboard((300, 260))

screen.onkey(pad1.move_up, 'w')
screen.onkey(pad1.move_down, 's')
screen.onkey(pad2.move_up, 'Up')
screen.onkey(pad2.move_down, 'Down')

run = True

while run:

    screen.update()
    time.sleep(ball.move_speed)

    # Moving Ball
    ball.move()

    # Detection Upper and Lower Wall = Bounce
    ball.detect_ycor()

    # Detect if ball is out of bound.
    ball.out_of_bound_pad1()
    ball.out_of_bound_pad2()

    # Adding points
    if ball.xcor() == -380:
        score_pad2.points_pad2()

    if ball.xcor() == 380:
        score_pad1.points_pad1()

    # Detect if ball hits paddles
    if ball.xcor() > 360 and ball.distance(pad2) < 50 or ball.xcor() < -360 and ball.distance(pad1) < 50:
        ball.bounce_x()

    # Game over!
    if score_pad1.s_pad1 == 10:
        run = False
        score_pad1.game_over('player1')

    if score_pad2.s_pad2 == 10:
        run = False
        score_pad2.game_over('player2')

screen.exitonclick()
