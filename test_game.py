#test_game.py

#play_game.py

import random
import string
from utility_functions import *
#functions

fileObj = open("wordle-answers-alphabetical.txt", "r")
answer_words = fileObj.read().splitlines()
fileObj.close()
fileObj = open("wordle-acceptable.txt", "r")
guess_words = fileObj.read().splitlines()
fileObj.close()

def get_word() -> str: #reads wordle-answers-alphabetical.txt file and selects a word at random from that file, then returns it
    num_words = len(answer_words)
    random_int = random.randint(0, num_words-1)
    word = answer_words[random_int]
    return word

def get_guess() -> str:
    while True:
        guess = input("Your Guess -> ").lower()
        if len(guess) == 5 and guess.isalpha() and guess in guess_words:
            return guess
        else:
            print("Input not appropriate length or contains non-alphabetic characters or guess not in word list.")

def play_game(answer: str):
    answer_set = set(answer)
    letter_list = list(string.ascii_lowercase)
    letter_list.sort()
    guess_number = 1
    fb = Feedback()

    while guess_number <= 6:
        print(letter_list)
        guess = get_guess()
        if guess == answer:
            print("You win! " + guess + " Was Correct!")
            return
        else:
            temp = "     "
            letters_not_in = set()
            for i in range(5):
                if guess[i] == answer[i]:
                    temp = temp[:i] + guess[i].upper() + temp[i+1:]
                elif guess[i] in answer_set:
                    temp = temp[:i] + guess[i] + temp[i+1:]
                if guess[i] not in answer_set:
                    letters_not_in.add(guess[i])
                if guess[i] in letter_list:
                    letter_list.remove(guess[i])
            fb.update(temp, letters_not_in)
            print(temp + " " + str(guess_number))
        
        #print("the guess is: " + guess + " the number is: " + str(guess_number))
        
        guess_number += 1

    print("You lose. The word was: " + answer.upper())

def test_game():
    #print("New Game Started")
    answer = get_word()
    play_game(answer)

    