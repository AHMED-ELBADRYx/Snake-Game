from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.appear()

    def appear(self):
        random_x = random.randint(-380, 380)
        random_y = random.randint(-340, 320)
        self.goto(random_x, random_y)