import random

options = ["rock", "paper", "scissors"]
stats = {"wins": 0, "ties": 0, "losses": 0}


while True:
    choice = input("Rock, paper, or scissors? Hit q to quit ").lower()
    computer_choice = options[random.randint(0, 2)]
    if choice == "q":
        break
    elif choice == computer_choice:
        print(f"The computer also picked {choice}, you have tied")
        stats["ties"] += 1
    elif choice == "rock":
        if computer_choice == "paper":
            print(
                f"The computer has chosen {computer_choice}, you have been defeated")
            stats["losses"] += 1
        elif computer_choice == "scissors":
            print(f"the computer has chosen {computer_choice}, you have won!")
            stats["wins"] += 1
    elif choice == "paper":
        if computer_choice == "scissors":
            print(
                f"The computer has chosen {computer_choice}, you have been defeated")
            stats["losses"] += 1
        elif computer_choice == "rock":
            print(f"the computer has chosen {computer_choice}, you have won!")
            stats["wins"] += 1
    elif choice == "scissors":
        if computer_choice == "rock":
            print(
                f"The computer has chosen {computer_choice}, you have been defeated")
            stats["losses"] += 1
        elif computer_choice == "paper":
            print(f"the computer has chosen {computer_choice}, you have won!")
            stats["wins"] += 1
    else:
        print("Invalid input, please try again")

w = stats["wins"]
t = stats["ties"]
l = stats["losses"]

print(f"Game results: \n Wins: {w} \n Ties: {t} \n Losses: {l}")
