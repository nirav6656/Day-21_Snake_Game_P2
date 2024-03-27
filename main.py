from turtle import Turtle, Screen
import time
from snake import Snake
screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Python Game")
screen.tracer(0)

sheru = Snake()


screen.listen()

screen.onkey(sheru.up, "Up")
screen.onkey(sheru.down, "Down")
screen.onkey(sheru.left, "Left")
screen.onkey(sheru.right, "Right")



game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    sheru.move()

screen.exitonclick()