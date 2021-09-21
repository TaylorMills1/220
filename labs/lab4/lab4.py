"""
Name: Taylor Mills
lab4.py

Problem: Graphic Accumulations and displaying them

Certificate of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(40, 40), Point(20, 20))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        new = shape.clone()
        new.move(dx, dy)
        new.draw(win)
        shape.move(dx, dy)

    win.getMouse()
    win.close()


squares()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """

    # opening window
    width = 400
    height = 400
    win = GraphWin("rectangle", width, height)

    # getting corners of triangle from user
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    # drawing the rectangle
    tangle = Rectangle(p1, p2)
    tangle.draw(win)

    px1 = p1.getX()
    px2 = p2.getX()
    py1 = p1.getY()
    py2 = p2.getY()
    length = px2 - px1
    width = py2 - py1

    perimeter = 2 * (length + width)
    area = length * width

    inst_pt = Point(200, 200)
    instructions = Text(inst_pt, "perimeter")
    instructions.draw(win)

    inst_pt = Point(200, 250)
    instructions = Text(inst_pt, "area")
    instructions.draw(win)

    inst_pt = Point(250, 200)
    instructions = Text(inst_pt, perimeter)
    instructions.draw(win)

    inst_pt = Point(250, 250)
    instructions = Text(inst_pt, area)
    instructions.draw(win)

    # closing window
    win.getMouse()
    win.close()

    pass


rectangle()


def circle():
    win = GraphWin("circle", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    px1 = p1.getX()
    py1 = p1.getY()
    px2 = p2.getX()
    py2 = p2.getY()
    d1 = (px2 - px1)**2
    d2 = (py2 - py1)**2
    d3 = d1 + d2
    distance = math.sqrt(d3)
    circle1 = Circle(p1, distance)
    circle1.setOutline("red")
    circle1.setFill("red")
    circle1.draw(win)

    # to print radius
    inst_pt = Point(250, 250)
    instructions = Text(inst_pt, distance)
    instructions.draw(win)

    win.getMouse()
    win.close()


circle()


def pi2():
    n = eval(input("number of terms:"))
    pi = 1
    pi1 = 1
    switch = 0
    for i in range(1, n + 1, 2):
        x = 4/n
        pi = pi + (x * -1)
    for i in range(2, n, 2):
        x = 4/n
        pi1 = pi1 + x
    print(pi + pi1)


pi2()


def main():
    squares()
    # rectangle()
    # circle()
    # pi2()


main()
