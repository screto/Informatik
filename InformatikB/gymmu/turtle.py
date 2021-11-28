import time

from ipycanvas import Canvas
from math import cos, sin, radians


class Turtle:
    direction = 0
    color = "black"
    drawing = True
    stroke_width = 1

    def __init__(self, x_max=400, y_max=400):
        self.canvas = Canvas(width=x_max, height=y_max, sync_image_data=True)
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
        self.direction = (self.direction - degree) % 360

    def reset(self):
        self.x_pos = 200
        self.y_pos = 200
        self.direction = 0
        self.set_color("black")
        self.set_stroke_width(1)

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
        self.canvas = Canvas(width, height, sync_image_data=True)

    def set_stroke_width(self, width):
        self.canvas.line_width = width

    def save_to_file(self, filename):
        self.canvas.to_file(filename)


turtle = Turtle()


def make_turtle():
    """Create a new turtle."""
    global turtle
    turtle = Turtle()


def forward(steps=50):
    """Move the turtle forward."""
    turtle.forward(steps)


def turn(degree=90):
    """Let the turtle turn in counter clockwise direction."""
    turtle.turn(degree)


def show():
    """Show the image which the turtle drew."""
    return turtle.show()


def clear():
    """Clear the image."""
    turtle.clear()


def reset():
    """Reset the turtle to the initial position."""
    turtle.reset()


def color(color):
    """Select the color which the turtle uses to draw."""
    turtle.set_color(color)


def pen_up():
    """Tell the turtle not to draw when it moves."""
    turtle.pen_up()


def pen_down():
    """Tell the turtle to draw when is moves."""
    turtle.pen_down()


def sleep(secs):
    """Wait until the next action is executed."""
    time.sleep(secs)


def is_inside_boundries():
    return turtle.is_inside_boundries()


def get_x_pos():
    """Get the current x position for the turtle."""
    return turtle.get_x_pos()


def get_y_pos():
    """Get the current y position for the turtle."""
    return turtle.get_y_pos()


def set_canvas_size(width, height):
    """Set the size of the canvas on which the turtle draws."""
    global turtle
    turtle = Turtle(width, height)


def stroke_width(width):
    turtle.set_stroke_width(width)


def save_image(filename):
    turtle.save_to_file(filename)
