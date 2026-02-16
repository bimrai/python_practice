import random

# options for user
choices = ['rock', 'paper', 'scissors']


# loop for game to continue with all the logic within to keep game running until if condition meets "quit" user input
while True:
    
    # takes in input to comapre with choices 
    user = input('Type in rock, paper or scissors: ').lower()
    
    # exit the game
    if user == "quit":
        print('Take care! :)')
        break
    
    # checks option to catch errors or invalid inputs
    if user not in choices:
        print('Invalid input!')
        
    # computer or opponent randomly selects one of the elements from choices list
    computer = random.choice(choices)
    
    # the logic behind the pairing between user and computer checking if user won, lost or drew
    if user == computer:
        print("You: " + user + " Computer: " + computer + " \n -----> DRAW! <-----")
    elif user == "rock" and computer == "scissors":
        print("You: " + user + ", Computer: " + computer + " \n -----> YOU WIN! <-----")
    elif user == "scissors" and computer == "rock":
        print("You: " + user + ", Computer: " + computer + " \n -----> YOU LOST! <-----")
    elif user == "scissors" and computer == "paper":
        print("You: " + user + ", Computer: " + computer + " \n -----> YOU WIN! <-----")
    elif user == "rock" and computer == "paper":
        print("You: " + user + ", Computer: " + computer + " \n -----> YOU LOST! <-----")
    elif user == "paper" and computer == "rock":
        print("You: " + user + ", Computer: " + computer + " \n -----> YOU WIN! <-----")
    elif user == "paper" and computer == "scissors":
        print("You: " + user + ", Computer: " + computer + " \n -----> YOU LOST! <-----")