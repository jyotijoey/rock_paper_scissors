import random
user_input = input('"rock", "paper", "scissors" ')
possible_choices = ["rock", "paper", "scissors"]

computer_choice = random.choice(possible_choices)

print(f"you chose {user_input} user_input, computer chose {computer_choice}")

result = ""

if(user_input == computer_choice):
    result = "draw"
elif(user_input == "rock"):
    if(computer_choice != "paper"):
        result = "user won"
    else:
        result = "user lost"
elif(user_input == "paper"):
    if(computer_choice != "scissors"):
        result = "user won"
    else:
        result = "user lost"
elif(user_input == "scissors"):
    if(computer_choice != "rock"):
        result = "user won"
    else:
        result = "user lost"

print(result)