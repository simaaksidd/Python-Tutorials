import random
#Rock paper scissors game.
print("Can you beat me in rock paper scissors?")
user_score = 0
comp_score = 0
# rock = 0, paper = 1, scissors = 2
while True:
    choices = ["rock", "paper", "scissors"]
    user_input = input("Type Rock, Paper, Scissors, or q to quit: ")
    if user_input == "q":
        if user_score > comp_score:
            print("Goodbye! I'll beat you next time >:(")
        elif user_score == comp_score:
            print("Leaving on a tie?? I want to know who wins, though :(")
        else:
            print("Hahaha!!! Just as expected. See ya!")
        quit()
    if user_input not in choices:
        continue
    random_choice = random.randint(0,2)
    comp_choice = choices[random_choice]
    if user_input == "rock" and comp_choice == "scissors":
        print("I chose " + comp_choice + ". You Win!")
        user_score+= 1
    if user_input == "rock" and comp_choice == "paper":
        print("I chose " + comp_choice + ". I Win!")
        comp_score+= 1
    if user_input == "scissors" and comp_choice == "paper":
        print("I chose " + comp_choice + ". You Win!")
        user_score+= 1
    if user_input == "scissors" and comp_choice == "rock":
        print("I chose " + comp_choice + ". I Win!")
        comp_score+= 1
    if user_input == "paper" and comp_choice == "scissors":
        print("I chose " + comp_choice + ". I Win!")
        comp_score+= 1
    if user_input == "paper" and comp_choice == "rock":
        print("I chose " + comp_choice + ". You Win!")
        user_score+= 1
    if user_input == comp_choice:
        print("I chose " + comp_choice + ". tie!")
    print("My score: " + str(comp_score))
    print("Your score: " + str(user_score))
    continue
