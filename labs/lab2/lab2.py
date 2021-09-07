import math
"""
Name: Taylor Mills
arithmetic.py

problem: demonstrate how to execute arithmetic functions
"""


def sum_of_threes():
    upper_bound = eval(input("Enter upper bound: "))
    total = 0
    for i in range(3, upper_bound + 1, 3):
        total = total + i
    print(total)


sum_of_threes()


def triangle_area():
    a = eval(input("Enter side 1: "))
    b = eval(input("Enter side 2: "))
    c = eval(input("Enter side 3: "))
    s = (a + b + c) / 2
    area = s * (s - a) * (s - b) * (s - c)
    total_area = math.sqrt(area)
    print(total_area)


def multiplication_table():
    print("1  ", "2  ", "3  ", "4  ", "5  ", "6  ", "7  ", "8  ", "9  ", "10")
    for row in range(1, 11):
        for col in range(1, 11):
            print(row*col, end="\t")
        print()


multiplication_table()


triangle_area()


def sum_squares():
    start = eval(input("Enter start of range: "))
    end = eval(input("Enter end of range: "))
    total = 0
    for i in range(start, end + 1):
        total = total + i**2
    print(total)


sum_squares()


def power():
    base = eval(input("Enter base: "))
    exponent = eval(input("Enter exponent: "))
    total = 1
    for i in range(exponent):
        total = total * base
    print(total)


power()
