from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.get_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 320)
        self.hideturtle()
        self.update_scoreboard()

    def get_highscore(self):
        try:
            with open("Snake_highscore.txt", "r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            # If file doesn't exist or contains invalid data, return 0
            return 0

    def save_highscore(self):
        with open("Snake_highscore.txt", "w") as file:
            file.write(str(self.highscore))

    def update_scoreboard(self):
        self.write(f"High score: {self.highscore} \nScore: {self.score}", align = "center", font = ("arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.screen.bgcolor("darkred")
        self.goto(0, 0)

        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
            
        self.write(f"----------- Game Over ----------- \n\nFinally Score: {self.score} \n\nHigh score: {self.highscore}", align = "center", font = ("arial", 20, "normal"))