"""
Name: Taylor Mills
greeting.py

Problem: create a heart greeting card

Certificate of Authenticity:
I certify that this assignment is entirely my own work.
With the help of lots of research on functions
"""
import turtle


love = turtle.Turtle()


def bump():
    for i in range(200):
        love.right(1)
        love.forward(1)


def heart():
    love.fillcolor('pink')
    love.begin_fill()
    love.left(140)
    love.forward(113)
    bump()
    love.left(120)
    bump()
    love.forward(112)
    love.end_fill()


def be_mine():
    love.up()
    love.setpos(-20, 100)
    love.down()
    love.color('red')
    love.write("Be Mine!")


def arrow():
    love.fillcolor('pink')
    love.begin_fill()
    love.left(90)
    love.end_fill()


heart()
be_mine()
love.ht()
arrow()
turtle.bye()
