import turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(turtle.Turtle):

    def __init__(self, position):
        super().__init__()
        self.s_pad1 = 0
        self.s_pad2 = 0
        self.color('white')
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.scores_pad1()
        self.scores_pad2()

    def scores_pad1(self):
        self.write(f'Score: {self.s_pad1}', align=ALIGNMENT, font=FONT)

    def scores_pad2(self):
        self.write(f'Score: {self.s_pad2}', align=ALIGNMENT, font=FONT)

    def points_pad1(self):
        self.s_pad1 += 1
        self.clear()
        self.scores_pad1()

    def points_pad2(self):
        self.s_pad2 += 1
        self.clear()
        self.scores_pad2()

    def game_over(self, player):
        self.goto(0, 0)
        self.write(f'Game over! {player} won', align=ALIGNMENT, font=FONT)
