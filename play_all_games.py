#very_fast_first_word.py

#uses novel algorithm to solve difficult problem of wordle.
#idea is that the value of a piece of feedback is inherent in its frequency, and the number of words removed by a piece of feedback 
# to its frequency will be the abs(words_total_len - word_removed_len)
#additionally, this can be sped up by, as the previous method of maintaining a dictionary of feedbacks and their frequency is now 
# replaced by a dictionary where feedback is the key and the list of words that would not be removed is the value
#next iteration will be to precalculate the lowokup tables for each word/feedback combination (perhaps save to text file of some kind)
from collections import Counter
from random import randrange

def get_feedback(word: str, answer_word: str) -> str:
    feedback_arr = ['n']*len(word)
    answer_word_dict = Counter(answer_word)
    letters_marked_in = dict()
    for i in range(len(word)):
        if word[i] == answer_word[i]:
            feedback_arr[i] = 'g'
            if word[i] not in letters_marked_in:
                letters_marked_in[word[i]] = 0
            letters_marked_in[word[i]] += 1

    for i in range(len(word)):
        if word[i] != answer_word[i] and word[i] in answer_word:
            if word[i] not in letters_marked_in:
                letters_marked_in[word[i]] = 0
            if letters_marked_in[word[i]] < answer_word_dict[word[i]]:
                feedback_arr[i] = 'y'
                letters_marked_in[word[i]] += 1
    
    feedback = ''.join(feedback_arr)

    return feedback
    
def get_EIG(guess: str, answers: list):
    feedback = dict()
    for answer in answers:
        fb = get_feedback(guess, answer)
        if fb not in feedback:
            feedback[fb] = list()
        feedback[fb].append(answer)

    eig = 0
    """
    with open("initialwordlists.csv", "a") as file:
        file.write(guess + ",")
        for fb in feedback:
            file.write(fb.upper() + ",")
            temp = feedback[fb]
            for word in temp:
                file.write(word + ",")
        file.write("\r\n")
    """
    
    for fb in feedback:
        probability = len(feedback[fb])/2315
        pct_words_removed = (2315-len(feedback[fb]))/2315
        temp_eig = probability*pct_words_removed
        eig += temp_eig

    return eig

def get_best_guess(guesses: list, answers: list) -> str:
    #guesses = guesses[0:999] #for quick debugging of a shorter list < 1/10 size of original
    guesses = dict.fromkeys(guesses)
    
    for i, guess in enumerate(guesses):
        guesses[guess] = get_EIG(guess, answers)
        #if i%100 == 0:
        #print("Evaluate " + guess)
        #if i == 999:
        #    break

    best_guess = max(guesses, key = guesses.get)

    #print("got guesses, best guess is : " + best_guess)

    #guesses.remove(best_guess)
    """
    for i in range(1,101):
        best_guess = max(guesses, key = guesses.get)
        best_guess_eig = guesses.pop(best_guess)
        print(str(i) + " " + best_guess + "..." + str(best_guess_eig))

    #for i in range(1, 11):
    #    worst_guess = min(guesses, key = guesses.get)
    #    worst_guess_eig = guesses.pop(worst_guess)
    #    print(str(i) + " " + worst_guess + "..." + str(worst_guess_eig))
    """

    return best_guess

def take_turn(guesses: list, answers: list, target: str) -> list:
    best_guess = get_best_guess(guesses, answers)
    #print("Trying guess: " + best_guess)
    feedback = get_feedback(best_guess, target)
    temp_answers = []

    for answer in answers:
        if get_feedback(best_guess, answer) == feedback:
            temp_answers.append(answer)

    return temp_answers
    

def play_game(answers: list, guesses: list, target: str) -> int:
    

    best_guess = "roate"
    feedback = get_feedback(best_guess, target)
    temp_answers = []

    for answer in answers:
        temp = get_feedback(best_guess, answer)
        if temp == feedback:
            temp_answers.append(answer)

    answers = temp_answers
    for i in range(1,7):
        if len(answers) == 1:
            i += 1
            print("Got " + target + " in " + str(i) + " turns!")
            return i
        answers = take_turn(guesses, answers, target)

    print("Did not get " + target.upper())
    return -1
    

def main():
    fileObj = open("wordle-answers-alphabetical.txt", "r")
    answers = fileObj.read().splitlines()
    answers.sort()
    fileObj.close()
    fileObj = open("wordle-answers-alphabetical.txt", "r")
    guesses = fileObj.read().splitlines()
    guesses.sort()
    fileObj.close()

    #target_word_index = randrange(0, len(answers)-1)
    #target_word = answers[target_word_index]

    total_guesses = 0
    total_games = 0
    fail_count = 0
    fail_words = []
    num_games_to_play = len(answers)

    for i, answer in enumerate(answers):
        print(str(i) + " " + answer)
        total_games += 1
        guesses_count = play_game(answers, guesses, answer)
        if guesses_count == -1:
            fail_count += 1
            fail_words.append(answer)
        else:
            total_guesses += guesses_count

    print("Average number of turns across all games was " + str(total_guesses/total_games))

if __name__ == "__main__":
    main()