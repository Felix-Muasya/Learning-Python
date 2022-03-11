def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("\n" + key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, D) ").upper()

        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)


# ------------------------------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0


# ------------------------------------------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------------------")
    print("Results")
    print("-------------------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()
    print("Guesses ", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is " + str(score) + "%")
    if score == 0:
        print("You failed all the questions")
    elif score == 25:
        print("Please do better")
    elif score == 50:
        print("Average score")
    elif score == 75:
        print("Congratulations, good work")
    else:
        print("Excellent work!")


# ---------------------------- -----------------------------------

def play_again():
    response = input("Do you want to play again? (Y,N)").upper()
    if response == "Y":
        return True
    else:
        return False


# --------------------------------------------------------------------
questions = {
    "1. Who created Python?  ": "A",
    "2. What year was Python created?  ": "B",
    "3. Python is attributed to which comedy group?  ": "C",
    "4. Is the Earth round?  ": "A"
}
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smash", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]

new_game()
while play_again():
    new_game()

print("Bye Bye now")
