import random

possible_action = ["rock", "paper", "scissors"]

while True:
    user_input = input("enter a choice (R, P,S) : ")
    computer_action = random.choice(possible_action)
    #print(computer_action)
    #print(user_input)
    if (user_input == "R"):
        user_input = "rock"
    elif (user_input == "P"):
        user_input = "paper"
    elif (user_input == "S"):
        user_input = "scissors"
    else:
        continue
    if(user_input == "rock" and computer_action == "scissors") or (user_input == "scissors" and computer_action == "paper") or (user_input == "paper" and computer_action == "rock"):
        print(f"Player,{user_input}")
        print("You win")
        break


    elif(computer_action == "rock" and user_input == "scissors") or (computer_action == "scissors" and user_input == "paper") or (computer_action == "paper" and user_input == "rock"):
            print(f"Player,{computer_action}")
            print("You loose")
            break

    else:
        print("it is a tie")
        continue