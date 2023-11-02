import turtle


class Paddles(turtle.Turtle):

    def __init__(self, position):
        super().__init__()
        self.y = self.ycor()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=0.5)
        self.penup()
        self.goto(position)

    def player1_start(self):
        self.goto(-370, 0)

    def player2_start(self):
        self.goto(370, 0)

    def move_up(self):
        if self.ycor() > 235:
            pass
        else:
            self.sety(self.y)
            self.y += 40

    def move_down(self):
        if self.ycor() < -235:
            pass
        else:
            self.y -= 40
            self.sety(self.y)
