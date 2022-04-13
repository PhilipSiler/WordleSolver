#classes.py

## feedback class: defines an individual piece of feedback from a guess. The feedback consists of a set of confirmed_letters_in, which are letters that are confirmed to be in the word, 
## defines an individual piece of feedback from a guess.
## consists of:
## SET confirmed_letters_in, which are letters that are confirmed to be in the word. 
## SET confirmed_letters_out, which are letters that are confirmed. 
## STR confirmed_letters_place, which is a string consisting of white space " " characters and letters which are certainly in the word.

class Feedback:
    #def __init__(self, confirmed_letters_in: set, confirmed_letters_out: set, confirmed_letters_place: str):
    #    self.confirmed_letters_in = confirmed_letters_in
    #    self.confirmed_letters_out = confirmed_letters_out
    #    self.confirmed_letters_place = confirmed_letters_place

    def __init__(self):
        self.confirmed_letters_in = set()
        self.confirmed_letters_out = set()
        self.confirmed_letters_place = list("     ")

    def update(self, temp: str, letters_not_in: set):
        for i, c in enumerate(temp):
            if c.isalpha:
                if c.isupper:
                    self.confirmed_letters_place[i] = c
                if c.islower:
                    self.confirmed_letters_in.add(c)

        for c in letters_not_in:
            if c not in self.confirmed_letters_out:
                self.confirmed_letters_out.add(c)