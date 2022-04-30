#classes.py
class FastFeedback:
    def __init__(self, word: str):
        self.word = word
        self.feedback_freq = dict()




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
        self.confirmed_letters_place = [None]*5

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

    def remove_answers_helper(self, word: str) -> bool:
        word_set = set(word)
        for c in self.confirmed_letters_in:
            if c not in word_set:
                return True
                #answer_words.remove(word)

        #compare confirmed letters OUT
        for c in self.confirmed_letters_out:
            if c in word_set:
                return True
                #answer_words.remove(word)

        #compare confirmed letters that are IN their correct place:
        for i, c in enumerate(self.confirmed_letters_place):
            if c is not None:
                if word[i] != c.lower():
                    return True
                    #answer_words.remove(word)

    #checks list of answer words for compatibility with existing feedback. Compares letters that are confirmed NOT in, letters that are confirmed IN, and letters that are confirmed OUT
    def remove_answers(self, answer_words: list) -> list:
        answer_words_len = len(answer_words)
        words_to_remove = []
        for word in answer_words:
            if self.remove_answers_helper(word):
                words_to_remove.append(word)
            #compare confirmed letters IN

        #remove all words saved to the set
        for word in words_to_remove:
            answer_words.remove(word)
        answer_words_len_after_removal = len(answer_words)
        print("Potential Answers Reduced From " + str(answer_words_len) + " to " + str(answer_words_len_after_removal))
        return answer_words

    def remove_answers_float(self, answer_words: list) -> float:
        answer_words_len = len(answer_words)
        words_to_remove = []
        for word in answer_words:
            if self.remove_answers_helper(word):
                words_to_remove.append(word)

        return len(words_to_remove)/answer_words_len

