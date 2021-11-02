"""
Name: Taylor Mills
conditionals.py
"""


def addten(*nums):
    # Add ten to every number in the list
    return(x + 10 for x in nums)


def squareeach(*nums):
    return(x ** 2 for x in nums)


def sumlist(*nums):
    total = sum(nums)
    return total


def tonumbers(*strlist):
    return(int(x) for x in strlist)


def writesumofsquares():
    print()


def starter():
    weight = eval(input("Enter weight: "))
    numwins = eval(input("Enter wins: "))
    if ((160 > weight >= 150) and (numwins >= 5)) or (weight > 199) or (numwins > 20):
        print("starter")
    else:
        print("not starter")


def leapyear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(year, "is a leap year")
            else:
                print(year, "is not a leap year")
        else:
            print(year, "is a leap year")
    else:
        print(year, "is not a leap year")


def circlesoverlap():
    print()
