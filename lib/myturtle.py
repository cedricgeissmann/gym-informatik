import time

from ipycanvas import Canvas
from math import cos, sin, radians


class Turtle:
    direction = 0
    color = "black"
    drawing = True

    def __init__(self, x_max=400, y_max=400):
        self.canvas = Canvas(width=x_max, height=y_max)
        self.x_max = x_max
        self.x_pos = x_max / 2
        self.y_max = y_max
        self.y_pos = y_max / 2

    def forward(self, steps=50):
        x_end, y_end = self.calculate_endpoint(steps)
        if self.is_pen_down():
            self.canvas.stroke_line(self.x_pos, self.y_pos, x_end, y_end)
        self.x_pos = x_end
        self.y_pos = y_end

    def calculate_endpoint(self, steps):
        new_x = cos(radians(self.direction)) * steps + self.x_pos
        new_y = sin(radians(self.direction)) * steps + self.y_pos
        return (new_x, new_y)

    def turn(self, degree):
        self.direction = (self.direction + degree) % 360

    def reset(self):
        self.x_pos = 200
        self.y_pos = 200
        self.direction = 0
        self.set_color("black")

    def clear(self):
        self.canvas.clear()

    def show(self):
        self.canvas.fill_style = "green"
        self.canvas.fill_rect(self.x_pos - 2, self.y_pos - 2, 4, 4)
        self.canvas.fill_style = self.color
        self.canvas.stroke_style = self.color
        return self.canvas

    def set_color(self, color):
        self.color = color
        self.canvas.fill_style = self.color
        self.canvas.stroke_style = self.color

    def is_pen_down(self):
        return self.drawing

    def pen_up(self):
        self.drawing = False

    def pen_down(self):
        self.drawing = True

    def is_x_inside_boundries(self):
        return self.x_pos >= 0 and self.x_pos < self.x_max

    def is_y_inside_boundries(self):
        return self.y_pos >= 0 and self.y_pos < self.y_max

    def is_inside_boundries(self):
        return self.is_x_inside_boundries() and self.is_y_inside_boundries()

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos

    def set_canvas_size(self, width, height):
        self.canvas = Canvas()


turtle = Turtle()


def make_turtle():
    global turtle
    turtle = Turtle()


def forward(steps=50):
    turtle.forward(steps)


def turn(degree=90):
    turtle.turn(degree)


def show():
    return turtle.show()


def clear():
    turtle.clear()


def reset():
    turtle.reset()


def color(color):
    turtle.set_color(color)


def pen_up():
    turtle.pen_up()


def pen_down():
    turtle.pen_down()


def sleep(secs):
    time.sleep(secs)


def is_inside_boundries():
    return turtle.is_inside_boundries()


def get_x_pos():
    return turtle.get_x_pos()


def get_y_pos():
    return turtle.get_y_pos()


def set_canvas_size(width, height):
    global turtle
    turtle = Turtle(width, height)
