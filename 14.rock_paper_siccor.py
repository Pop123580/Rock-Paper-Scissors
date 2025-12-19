import random

def get_user_choice():
    return input("Choose rock, paper, or scissors: ").lower()

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
        (user == "scissors" and computer == "paper") or \
        (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

user = get_user_choice()
computer = get_computer_choice()

print("Computer chose:", computer)
print(decide_winner(user, computer))