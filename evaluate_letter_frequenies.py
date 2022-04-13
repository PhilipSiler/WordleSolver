#valuate_letter_frequencies.py




def evaluate_letter_frequencies():
    fileObj = open("wordle-answers-alphabetical.txt", "r")
    all_answers = ""

    for line in fileObj:
        all_answers += line.strip()
    
    letter_frequencies = {}

    for c in all_answers:
        if c not in letter_frequencies:
            letter_frequencies[c] = 1
        else:
            letter_frequencies[c] = letter_frequencies[c] + 1

    print(letter_frequencies)