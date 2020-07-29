#!/bin/python3

from random import randint as ri

player = input("Choose the following options:\n\nRock - R\nPaper - P\nScissors - S\n-->")
print('')

chosen_number = ri(1,3)

#print(chosen_number)

if chosen_number == 1:
    computer = 'R'
elif chosen_number == 2:
    computer = 'P'
elif chosen_number == 3:
   computer = 'S'
else:
    print("Please choose one of the options above(R,P ou S:")

#print(computer)
print(player,' vs ',computer)

if player == computer:
    print("Draw...\nPlay again and finish this!")
elif player == 'R'and computer =='S':
    print("You WON! Rock destroy Scissors!")
elif player == 'R'and computer =='P':
    print("You LOSE! Paper wraps Rock!")
elif player == 'P'and computer =='S':
    print("You LOSE! Paper wraps Rock!")
elif player == 'P'and computer =='':
    print("You LOSE! Paper wraps Rock!")
elif player == 'S'and computer =='P':
    print("You LOSE! Paper wraps Rock!")
elif player == 'S'and computer =='P':
    print("You LOSE! Paper wraps Rock!")
else:
    print(player+"WHAT???")