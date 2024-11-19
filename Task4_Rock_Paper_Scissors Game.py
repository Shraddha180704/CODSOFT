import random
import sys

user_score = 0
computer_score = 0

def game_rules(user_choice, comp_choice):
    global user_score
    global computer_score

    if user_choice == "exit":
        sys.exit()

    if (user_choice == "scissor" and comp_choice == "paper") or (user_choice == "paper" and comp_choice == "rock") or (user_choice == "rock" and comp_choice == "scissor"):
        user_score += 1
    else:
        computer_score += 1

    print(f"user choice: {user_choice} and computer choice: {comp_choice}")
    print(f"user score: {user_score} and computer score: {computer_score}")


def computer_choice():
    choices = ["rock", "paper", "scissor"]
    comp_choice = random.choice(choices)
    return comp_choice

def exit_game():
    global user_score
    global computer_score
    exit_choices = ["yes", "no"]
    exit_choice = input("Enter yes to exit from game else no: ")
    while exit_choice not in exit_choices:
        print("Invalid input(yes/no)")
        exit_choice = input("Enter yes to exit from game else no: ").lower()
    if exit_choice == "yes":
        sys.exit()
    else:
        user_score = 0
        computer_score = 0
        user_choices()



def display_result():
    if user_score > computer_score:
        print(f"User won!!, user score is: {user_score} and computer score is: {computer_score}\n")
    else:
        print(f"Computer won!!, user score is: {user_score} and computer score is: {computer_score}\n")

def user_choices():
    global user_score
    global computer_score
    i = 1
    print("ROCK PAPER SCISSOR")
    print("You need 5 points to win\n")
    while user_score < 5 and computer_score < 5:
        print("Round", i)
        choices = ["rock", "paper", "scissor", "exit"]
        user_choice = input("Enter your choice (rock/paper/scissor/exit): ")
        while user_choice not in choices:
            print("Invalid input")
            user_choice = input("Enter your choice (rock/paper/scissor/exit): ").lower()
        comp_choice = computer_choice()
        game_rules(user_choice, comp_choice)
        print()
        i += 1
    display_result()

    exit_game()


user_choices()