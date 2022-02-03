# Number generator
import random
numLists = []
def generator():
    numLists.append(random.randint(1, 9 + 1))
    return numLists

# User Input
print("Welcome to my guessing game. You will guess a number my program randomly picks form 1-9. ")
guessNum = None
def guess():
    guessNum = int(input("Guess the number: "))
    return guessNum

# Guess accuracy
def accuracy():
    guessNum = guess()
    while True:
        if guessNum > numLists[0]:
            print("Too high")
        if guessNum < numLists[0]:
            print("Too low")
        if guessNum == numLists[0]:
            print("Correct!")
            break
        guessNum = int(input("Guess the number again: "))

# Game Loop
while True:
    generator()
    accuracy()
    gameRestart = input("Enter 'r' to play again or 'e' to exit. ")
    if gameRestart == "r":
        continue
    else:
        if gameRestart == "e":
            break
print("Game Finished!")
