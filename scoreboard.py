from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.read_data()
        self.hideturtle()
        self.penup()
        self.setposition(x=0, y=270)
        self.color("white")
        self.speed("fastest")
        self.draw_score()

    def update_score(self):
        self.score += 1
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.read_data()}", align="center", font=("Courier", 15, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_data()
        self.score = 0
        self.draw_score()

    def write_data(self):
        with open("data.txt", "w", encoding="UTF-8") as file:
            file.write(str(self.highscore))

    def read_data(self):
        with open("data.txt", "r", encoding="UTF-8") as file:
            highscore = file.read()
            return int(highscore)
