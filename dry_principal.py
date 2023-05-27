# DRY ---> don't repeate yourself ------>

import random
winning_number=random.randint(1,1000)
guess=1
number=int(input("guess a number between 1 to 1000 :"))
game_over= False
while not game_over:
    if number==winning_number:
        print(f"you win the game and you guessed this number {guess} times .")
        break
    else:
        if number<winning_number:
            print("too low")   
        else:
            print("too high")
    guess+=1
    number=int(input("please guess again :"))


# another solution ---->

import random
winning_number=random.randint(1,1000)
guess=1
game_over= False
while not game_over:
    number=int(input("guess a number between 1 to 1000 :"))
    if number==winning_number:
        print(f"you win the game and you guessed this number {guess} times .")
        break
    else:
        if number<winning_number:
            print("too low")   
        else:
            print("too high")
    guess+=1
    continue