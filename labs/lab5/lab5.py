"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from graphics import *
import math


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    triang = Polygon(p1, p2, p3)
    triang.draw(win)

    px1 = p1.getX()
    px2 = p2.getX()
    px3 = p3.getX()
    py1 = p1.getY()
    py2 = p2.getY()
    py3 = p3.getY()
    dx1 = abs(px1 - px2)
    dy1 = abs(py1 - py2)
    dx2 = abs(px1 - px3)
    dy2 = abs(py1 - py3)
    dx3 = abs(px2 - px3)
    dy3 = abs(py2 - py3)
    a = math.sqrt(dx1**2 + dy1**2)
    b = math.sqrt(dx2**2 + dy2**2)
    c = math.sqrt(dx3**2 + dy3**2)
    perimeter = a + b + c
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    inst_pt = Point(200, 200)
    instructions = Text(inst_pt, perimeter)
    instructions.draw(win)
    inst_pt2 = Point(250, 250)
    instructions2 = Text(inst_pt2, area)
    instructions2.draw(win)

    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.

    # Wait for another click to exit
    win.getMouse()
    win.close()


triangle()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    strings = input("Input string: ")
    print(strings[0])
    print(strings[-1])
    print(strings[-1])
    print(strings[2:5])
    print(strings[0] + strings[-1])
    three = strings[0:3]
    print(three * 10)
    y = -1
    length = len(strings)
    for i in range(length):
        y = y + 1
        print(strings[y])
    print(length)


process_string()

def process_lists():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    # x = values[0] + values[2]
    # print(x)
    x = values[1 * 5]
    print(x)
    x = values[2:5]
    print(x)
    x = values[2] + values[3] + values[0]
    print(x)
    x = values[0 + 2] + 7.2
    print(x)
    x = len(values)
    print(x)


def another_series():
    inputs = eval(input("Enter number of terms: "))
    lists = [2, 4, 6]
    x = -1
    c = 1
    for i in range(inputs):
        x = x + 1
        y = lists[x]
        c = y * c
    print(x)


def main():
    # target()
    # triangle()
    # color_shape()
    pass


main()
