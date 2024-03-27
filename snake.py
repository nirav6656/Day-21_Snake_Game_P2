from turtle import Turtle, Screen
POSITIONS = [(-10, 0), (-20, 0), (-30, 0), (-40, 0)]
screen = Screen()
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.sheru_gang = []
        self.create_snake()
        self.head = self.sheru_gang[0]

    def create_snake(self):
        self.sheru_gang = []
        for position in POSITIONS:
            sheru = Turtle("square")
            sheru.speed(0)
            sheru.penup()

            sheru.color("white")
            sheru.goto(position)
            self.sheru_gang.append(sheru)

    def move(self):
        for seru_number in range(len(self.sheru_gang) - 1, 0, -1):
            newx = self.sheru_gang[seru_number - 1].xcor()
            newy = self.sheru_gang[seru_number - 1].ycor()
            self.sheru_gang[seru_number].goto(newx, newy)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)