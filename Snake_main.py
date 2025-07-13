from turtle import Turtle, Screen
import turtle  # For the exception handling
import tkinter # For the exception handling
from Snake_set import Snake
from Snake_food import Food
from Snake_score import Scoreboard
import time

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

game_on = True
try:
    while game_on:
        snake.move()
        screen.update()
        time.sleep(0.1)
        screen.listen()
        screen.onkey(snake.up, "Up")
        screen.onkey(snake.down, "Down")
        screen.onkey(snake.right, "Right")
        screen.onkey(snake.left, "Left")

        if snake.head.distance(food) < 15:
            food.appear()
            snake.extend()
            score.increase_score()

        if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
            game_on = False
            score.game_over()
            
        for segment in snake.turtles[:-1]: # --> Without the head
            if snake.head.distance(segment) < 10: # --> Head collision with the body
                game_on = False
                score.game_over()

    screen.exitonclick()
except (turtle.Terminator, tkinter.TclError):
    pass