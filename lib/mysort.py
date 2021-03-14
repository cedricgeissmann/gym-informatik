"""Helper functions for array sorting."""
from ipycanvas import Canvas, hold_canvas
from random import shuffle
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)


def color(col):
    canvas.fill_style = col


def make_canvas():
    global canvas
    canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    display(canvas)


def display_list(li):
    pos = 0
    min_elem = min(li)
    max_elem = max(li) + 1
    elem_diff = max_elem - min_elem
    elem_height = CANVAS_HEIGHT / elem_diff
    width = CANVAS_WIDTH / len(li)
    with hold_canvas(canvas):
        canvas.clear()
        for elem in li:
            rect_height = (elem - min_elem + 1) * elem_height
            canvas.fill_rect(0 + pos * width, 400 - rect_height, width, rect_height)
            pos += 1


def get_random_list(length):
    li = [i for i in range(length)]
    shuffle(li)
    return li


def sleep(sec):
    time.sleep(sec)


def bubble_sort_demo():
    li = get_random_list(20)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(li) - 1):
            if li[i] > li[i + 1]:
                tmp = li[i]
                li[i] = li[i + 1]
                li[i + 1] = tmp
                sorted = False
        display_list(li)
        sleep(0.2)
