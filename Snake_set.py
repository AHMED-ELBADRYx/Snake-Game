from turtle import Turtle

class Snake():
    def __init__(self):
        self.turtles = []
        self.POSITION = [(-40, 0), (-20, 0), (0, 0)]
        self.create_snake()
        self.head = self.turtles[-1]

    def create_snake(self):
        for i in range(len(self.POSITION)):
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(self.POSITION[i])
            self.turtles.append(new_turtle)

    def move(self):
            for i in range(len(self.turtles)-1):
                self.turtles[i].goto(self.turtles[i+1].pos())
            self.head.forward(20)

    def extend(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.turtles[0].pos())
        self.turtles.insert(0, new_segment)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)