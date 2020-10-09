"""
program 3/3, rock paper scissors
"""
from random import randint
text = ["Rock", "Paper", "Scissors", "rock", "paper", "scissors"]
computer = text[randint(0,2)] #Creates a random number that the computer uses to choose its play
PlayerN = input("Please enter your name: ")
computerN = input("Please enter the name of your opponite: ")

restart = True
CompW = int(0)
PlayW = int(0)
while restart == True: #allows for play again
    computer = text[randint(0,2)]
    player = input("Rock, Paper, Scissors? ")
    
    while player != 'Rock' and player != 'Paper' and player != 'Scissors' and player != 'rock' and player != 'paper' and player != 'scissors': 
        print("wrong type ") #checks if the input is correct and asks again
        player = input("Rock, Paper, Scissors? ")
   
    if player == computer: #starts the if statments to see which move the computer made vs player
            print("Tie!")
            print("computer wins ", CompW)
            print("player wins ", PlayW)
    elif player == "Rock" or "rock":
        if computer == "Paper":
            print("You Lose! ", computerN, " crushes the ", PlayerN)
            CompW += 1
            print("computer wins ", CompW)
            print("player wins ", PlayW)
        else:
            print("You WIN!", PlayerN, " crushed the ", computerN)
            PlayW += 1
            print("computer wins ", CompW)
            print("player wins ", PlayW)
    elif player == "Paper" or "paper":
        if computer == "Scissors":
            print("You Lose! ", computerN, " cut the ", PlayerN)
            CompW += 1
            print("computer wins ", CompW)
            print("player wins ", PlayW)
        else:
            print("You WIN! ", PlayerN, " covered ", computerN)
            PlayW += 1
            print("computer wins ", CompW)
            print("player wins ", PlayW)
    elif player == "Scissors":
        if computer == "Rock" or "rock":
            print("You Lose! ", computerN, " crushes the ", PlayerN)
            CompW += 1
            print("computer wins ", CompW)
            print("player wins ", PlayW)
        else:
            print("You WIN! ", PlayerN, " cut ", computerN)
            PlayW += 1
            print("computer wins ", CompW)
            print("player wins ", PlayW)
   
    play = input("Play again? y/n ") #asks to play again
    
    if play == 'y':
        restart = True
    else:
        restart = False
        print("Final score is player with", PlayW, "wins vs computer with", CompW, "wins")
