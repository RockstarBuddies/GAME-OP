#2 Player Game
print("Welcome! Please Enter Your Names and Follow the instructions-")
import random
from math import *
Player1=input("Enter Player 1 Name: ")
Player2=input("Enter Player 2 Name: ")

if Player1==Player2:
     raise Exception('Both the Players cannot have the same name')
print('''The Game Proceeds as follows:-
         1.The Computer will generate a random number between 1 to 100 each time
         2.The Players will have to guess the number
         3.The person with the closest guess wins
         4. LET'S PLAY !!!!!!''')
z="Y"
while z=="Y" or z=="y":
    a=random.randint(0,100)
    a1=int(input("Random Guess of Player 1: "))
    b1=int(input("Random Guess of Player 2: "))
    if a1<0 or b1<0 or a1>100 or b1>100:
         raise ValueError
    print("Random Assortion Value = ",a)
    if abs(a1-a)<abs(b1-a):
         print("Winner is",Player1)
    elif abs(a1-a)==abs(b1-a):
         raise ValueError('Pls enter different guesses')
    elif abs(b1-a)< abs(a1-a):
         print("Winner is", Player2)
    elif abs(a1)==a or abs(b1)==a:
         print("ABSOLUTE WIN!!!! CONGRATULATIONS, YOU PICKED UP THE EXACT ANSWER")
    else:
        print("Thank You For Playing")
        break
    z=input("Do you want to play more?(Y/N): ")
    if z=="N" or z=="n":
         print("Thank You For Playing")
         break
