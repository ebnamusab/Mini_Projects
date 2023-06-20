import random
import math

print("Welcome to the game")
print("-----------------------")

lower = int(input("please enter lower limit: "))
upper = int(input("please enter upper limit: "))

guess = int(input("please guess the number: "))

if guess<lower or guess>upper:                  #this line for;if user input invalid number#
    print("Please enter your number between the range: ")
else:
    random_num = random.randint(lower, upper)               #this line for;if user input valid number# and import random module
    chance = round(math.log(upper-lower+1, 2) )                    #chance method and import the module# and #round for roundNumber

    while chance>0:         #this logic is how many times chance the user
        chance= chance-1
        if guess>random_num:
            print("You choose high")
        elif guess<random_num:
            print("You choose Low")
        else:
            print("You choose the right number", random_num)
            break
        if chance != 0:
            print("you have only",chance,"chances left")
            guess = int(input("please guess the number: "))
        else:
            print("You have lost the match")


