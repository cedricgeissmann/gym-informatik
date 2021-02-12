from ipycanvas import Canvas
from math import cos, sin, radians


class Turtle:
    canvas = Canvas(width=200, height=200)

    x_pos = 100
    y_pos = 100
    direction = 0

    def forward(self, steps=50):
        x_end, y_end = self.calculate_endpoint(steps)
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
        self.x_pos = 100
        self.y_pos = 100
        self.direction = 0

    def clear(self):
        self.canvas.clear()

    def show(self):
        return self.canvas
