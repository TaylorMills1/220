"""
Name: Taylor Mills
traffic.py

Problem: Calculate the average number of cars moving on different roads a day and the general average of all roads

Certificate of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main2():
    total = 0
    roads = eval(input("How many roads were surveyed? "))
    for _ in range(roads):
        days = eval(input("How many days was the road surveyed? "))
        for _ in range(days):
            cars = eval(input("How many cars traveled? "))
            total = cars + total
        print("Average vehicles per day: ", (total / days))
    print("Total number or vehicles traveled on all roads: ")
    print("Average number of vehicles per road: ")
