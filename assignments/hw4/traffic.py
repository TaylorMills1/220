"""
Name: Taylor Mills
traffic.py

Problem: Calculate the average number of cars moving on different roads a day and the general average of all roads

Certificate of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main2():
    roads = eval(input("How many roads were surveyed? "))
    time = 0
    days = 0
    for _ in range(roads):
        days = eval(input("How many days was the road surveyed? "))
        total = 0
        for _ in range(days):
            cars = eval(input("How many cars traveled? "))
            total = cars + total
        print("Total number of cars on this road: ", total)
        print("Average vehicles per day: ", (total / days))
        total = total - total
    print("Total number or vehicles traveled on all roads: ", grand)
    print("Average number of vehicles per road: ", (grand / days))
