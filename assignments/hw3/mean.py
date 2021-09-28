"""
Name: Taylor Mills
mean.py

Problem: developing a simple python program that asks for input, does arithmetic, & provides output.

Certificate of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


# This program will calculate the root mean square average harmonic mean & geometric mean
# inputs be the values & the outputs will be the harmonic geometric & the RMS average
# the program must: get values, run values through equations, print values
def main():
    variables = eval(input("Enter number of variables: "))
    sum1 = 0
    sum2 = 0
    sum3 = 1
    for _ in range(1, variables+1):
        new = eval(input("enter variable: "))
        sum1 = new**2 + sum1
        sum2 = (1 / new) + sum2
        sum3 = new * sum3
    fract1 = sum1 / variables
    rms = math.sqrt(fract1)
    print("Rms: ", round(rms, 3))
    fract2 = variables / sum2
    print("harmonic: ", round(fract2, 3))
    fract3 = math.pow(sum3, (1 / variables))
    print("geometric: ", round(fract3, 3))
