from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ls = 0
        self.rs = 0
        self.gg = 0
        self.color("white")
        self.hideturtle()
        self.goto(-100, 200)
        self.write(f"{self.ls}", move=False, align="center", font=("Times New Roman", 70, "normal"))
        self.goto(100, 200)
        self.write(f"{self.rs}", move=False, align="center", font=("Times New Roman", 70, "normal"))

    def update_sc(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.ls}", move=False, align="center", font=("Times New Roman", 70, "normal"))
        self.goto(100, 200)
        self.write(f"{self.rs}", move=False, align="center", font=("Times New Roman", 70, "normal"))

    def l_point(self):
        self.ls += 1
        self.update_sc()

    def r_point(self):
        self.rs += 1
        self.update_sc()

    def t_off(self):
        self.gg = 1

    def win(self):
        if self.ls > self.rs:
            self.goto(0, 0)
            self.color("red")
            self.write("PLAYER 1 WINS!", move=False, align="center", font=("Contantia", 50, "normal"))
            self.goto(0, -280)
            self.color("Pink")
            self.write("Made by Zikron", move=False, align="center", font=("Arial", 15, "normal"))
        elif self.rs > self.ls:
            self.goto(0, 0)
            self.color("Blue")
            self.write("PLAYER 2 WINS!", move=False, align="center", font=("Contantia", 50, "normal"))
            self.goto(0, -280)
            self.color("Pink")
            self.write("Made by Zikron", move=False, align="center", font=("Arial", 15, "normal"))
        else:
            self.goto(0, 0)
            self.color("Green")
            self.write("IT'S A DRAW!", move=False, align="center", font=("Contantia", 50, "normal"))
            self.goto(0, -280)
            self.color("Pink")
            self.write("Made by Zikron", move=False, align="center", font=("Arial", 15, "normal"))

