from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        self.file = open("highscore.txt")
        self.highscore = int(self.file.read())
        self.file.close()
        self.color("white")
        self.penup()
        self.wait = 0.25

        self.goto(0,320)
        self.update_score()

    def update_score(self):
        self.clear()
        self.highscore_check()
        self.write(f"Score :{self.score} High Score:{self.highscore}",  align="center", font=("Arial", 10, "normal"))

    def highscore_check(self):
        if self.score > self.highscore :
            self.highscore = self.score


    def reset(self):
        self.highscore_check()
        with open("highscore.txt", mode="w") as hisc:
            hisc.write(str(self.highscore))
        self.score = 0
        self.update_score()


    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()

    def speeder(self):
        for x in [10, 20 ,30, 40] :
            if self.score == x:
                self.wait -= 0.05
        return self.wait
