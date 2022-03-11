import random
while True:
    choices = ["Rock", "Paper", "Scissors"]

    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input ("Rock, Paper, or Scissors? ").capitalize()

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")

    elif player == "Rock":
        if computer == "Paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "Scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "Scissors":
        if computer == "Paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
        if computer == "Rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")

    elif player == "Paper":
        if computer == "Scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "Rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    play_again= input("Play again? (Yes, No): ").capitalize()
    if play_again!= "Yes":
        break
print ("Bye, see you later")






















