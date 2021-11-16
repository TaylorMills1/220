"""
Name: Taylor Mills
hangman.py
"""
import random
import re


def hangman():
    with open("wordlist.txt") as f:
        word_list = f.read().splitlines()

    number_of_lives = 7

    random_num = random.randint(0, len(word_list)-1)
    word_chosen = word_list[random_num]

    encoded_word = re.sub('abcdefghijklmnopqrstuvwxyz', '-', word_chosen)

    def guess(letter, word, encoded):
        found = False
        if letter in word:
            found = True
            for i in range(0, len(word)):
                if word[i] == letter:
                    encoded = encoded[0:i] + letter + encoded[i+1:len(encoded)]
            return found, encoded
    print(encoded_word)

    while number_of_lives > 0:
        guessed_letter = input("Your guess: ")[:1]

        letter_found, encoded_word = guess(guessed_letter, word_chosen, encoded_word)

        if not letter_found:
            number_of_lives -= 1
            if number_of_lives == 0:
                print("\nLetter not found, game over. The word was %s" % word_chosen)
                break
            else:
                print("\nLetter not found. Tries left: %d" % number_of_lives)
                print(encoded_word)
        else:
            if "-" not in encoded_word:
                print("\nThe word was '%s'" % word_chosen)
                break
            else:
                print("Letter was found.")
                print(encoded_word)


hangman()
