import string
from play_game import * 
from evaluate_letter_frequenies import *
from utility_functions import *
from test_game import *

#MAIN Begins Below
def main():
    print("Welcome to Wordle")
    while True:
        menu_selection = input("Please enter what you would like to do:\r\n0 -> Exit\r\n1 -> New Game\r\n2 -> Play Test Game\r\n3 -> Get Letter Frequencies\r\n")
        match menu_selection:
            case '0' : exit()
            case '1' : new_game()
            case '2' : test_game()
            case '3' : evaluate_letter_frequencies()
            case _ : 
                print("Input not recognized.")
                main()

# Call Main
main()