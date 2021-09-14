"""
Name: Taylor Mills
lab3.py

Problem: Demonstrating how to use loop functions for arithmetic

Certificate of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    hw1 = eval(input("Enter your grade on HW1: "))
    hw2 = eval(input("Enter your grade on HW2: "))
    avr = (hw1 + hw2) / 2
    print("Your average grade is: ", avr)


average()


def tip_jar():
    tip = 0
    for i in range(1, 6):
        total = eval(input("Enter Tip Given: "))
        tip = tip + total
    print("Total tips: ", tip)


tip_jar()


def newton():
    x = eval(input("Enter x value: "))
    approxim = eval(input("Enter times to approximate: "))
    approx = x / 2
    for i in range(1, approxim + 1):
        approx = (approx + (x / approx)) / 2
    print("Approximated square root:", approx)


newton()


def sequence():
    dig = eval(input("Enter number of terms: "))
    number = 1
    for i in range(1, dig + 1):
        print(number)
        number = number + 2
        print(number)


sequence()


def pi():
    dig = eval(input("Enter desired number of digits: "))
    pies = 1
    for i in range(1, dig + 1):
        pie = ((2 * i) / ((2 * i) - 1)) * ((2 * i) / ((2 * i) + 1))
        pies *= pie
    print(pies * 2)


pi()
