import random

choiceList = ["Rock", "Paper", "Scissors"]
while True:
    compChoice = random.choice(choiceList)
    userChoice = input("Enter Your Choice: ")
    if userChoice == compChoice:
        print("Thats a tie.")
    elif userChoice == "Rock":
        if compChoice == "Paper":
            print("You Lost")
        elif compChoice == "Scissors":
            print("You Won")
    elif userChoice == "Paper":
        if compChoice == "Rock":
            print("You Won")
        elif compChoice == "Scissors":
            print("You Lost")
    elif userChoice == "Scissors":
        if compChoice == "Paper":
            print("You Won")
        elif compChoice == "Rock":
            print("You Lost")
    else:
        print("Enter a valid option.")
    newGame = input("Want To Play Again(y/n)?")
    if newGame == "n":
        break;