import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.y_move = 2
        self.x_move = 2
        self.move_speed = 0.01

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= .9

    def detect_ycor(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()

    def out_of_bound_pad2(self):
        if self.xcor() > 380:
            self.home()
            self.bounce_x()

    def out_of_bound_pad1(self):
        if self.xcor() < -380:
            self.home()
            self.bounce_x()
