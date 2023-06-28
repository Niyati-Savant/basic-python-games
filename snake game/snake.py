import turtle

COORDINATE = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in COORDINATE:
            self.add_segment(position)

    def add_segment(self, position):
        snake_obj = turtle.Turtle("square")
        snake_obj.penup()
        snake_obj.color("white")
        snake_obj.goto(position)
        self.snake_body.append(snake_obj)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for part in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[part - 1].xcor()
            new_y = self.snake_body[part - 1].ycor()
            self.snake_body[part].goto(new_x, new_y)
        self.head.forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for part in self.snake_body:
            part.goto(1000,1000)

        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]