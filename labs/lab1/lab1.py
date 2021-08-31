"""
Name: (Taylor Mills>
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area = ", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    shots = eval(input("Enter the number of total shots: "))
    scored = eval(input("Enter the number of shots made: "))
    percentage = (shots / scored) * 100
    print("Shooting Percentage =", percentage)


def coffee():
    price = 10.50
    shipping = 0.86
    fixed = 1.50
    pounds = eval(input("Enter total pounds ordered: "))
    total = (price * pounds) + fixed + (pounds * shipping)
    print("Total Cost =", total)


def kilometer_to_miles():
    miles = eval(input("Enter miles to travel: "))
    conversion = 1.61
    kilometers = miles * conversion
    print("Kilometers =", kilometers)
