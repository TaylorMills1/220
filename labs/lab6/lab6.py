"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input('Enter First and Last Name: ')
    first, last = name.split(" ")
    flip = ','.join([last, first])
    print(flip)


def company_name():
    website = input('Enter three-part domain name: ')
    weebsite = website.split(".")
    name = weebsite[2]
    print("Company name: ", name)


def initials():
    quantity = eval(input("How many names will be entered? "))
    for _ in range(quantity):
        first = input('Enter students first name: ')
        last = input('Enter students last name: ')
        print(first[0] + last[0])


def names():
    namess = input('Enter list of names separated by commas: ')
    lists = namess.split(",")
    for c in namess:
        namess = lists.split()
        first = namess[0][0]



def thirds():
    sentences = eval(input("How many sentences will be input? "))
    for i in range(sentences):
        sentence = input('input sentence: ')
        print(sentence[::3])


def word_average():
    sentence = input("enter sentence: ")
    words = sentence.split()
    average = sum(len(word) for word in words) / len(words)
    print(average)


def pig_latin():
    words = input("Input Sentence:").split()
    for word in words:
        print(word[1:] + word[0] + "ay", end=" ")
    print()


def main():
    name_reverse()
    # add other function calls here


main()
