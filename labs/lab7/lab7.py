"""
Name:
Partner: <your partner's name goes here – first and last>
<ProgramName>.py
"""
import math


def cash_conversion():
    one = eval(input("Enter integer dollar amount: "))
    decimal = ('{0:5}'.format(one, '.2f'))
    print(decimal)


def encode():
    original = input("Enter OG text: ")
    shift = eval(input("Enter shift: "))
    text = ""
    for ch in original:
        if ch.isalpha():
            letters = ord(ch) + shift
            if letters > ord('z'):
                letters -= 26
            last = chr(letters)
            text += last
    print(text)


def sphere_area(radius):
    area = 4*math.pi*radius**2
    print(area)


def sphere_volume(radius):
    volume = 4//3*math.pi*radius**3
    print(volume)


def sum_n(n):
    sums = 0
    for i in range(0, n+1):
        num = i
        sums = sums + num
    print(sums)


def sum_n_cubes(n):
    sums = 0
    for i in range(0, n+1):
        num = i
        sums = sums + pow(num, 3)
    print(sums)


def encode_better():
    start = ord("a")
    code_word = input("Code word: ")
    original = input("OG Text: ")
    expandedcode_word = ""
    while len(expandedcode_word) < len(original):
        for i in code_word:
            if len(expandedcode_word) < len(original):
                expandedcode_word += i
    cipher = ''
    ahh = 0
    for i in original:
        if i == ' ':
            cipher = cipher + " "
        else:
            shift = ((ord(i) - start) + ord(expandedcode_word[ahh])-start) % 26 + start
            cipher = cipher + chr(shift)
            ahh = ahh + 1
    print(cipher)

