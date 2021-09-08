"""
Name: Taylor Mills
interest.py

Problem: Calculate the monthly interest paid on an account

Certificate of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    rate = eval(input("Enter annual interest rate percentage: "))
    cycle = eval(input("Enter length of billing cycle in days: "))
    balance = eval(input("Enter previous net balance of account: "))
    payment = eval(input("Enter payment amount: "))
    day = eval(input("Enter the day of the billing cycle that the payment was made on: "))
    monthly_rate = (((cycle * balance) - (payment * (cycle - day))) / cycle) * ((rate / 12) / 100)
    print(round(monthly_rate, ndigits=2))
