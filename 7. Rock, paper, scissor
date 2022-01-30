# Variables
rock = 'Rock'
paper = 'Paper'
scissor = 'Scissor'

# Player names
player_1 = input("Player one, what is your name? ")
player_2 = input("Player two, what is your name? ")

# Players choice
while True:
    player1_choice = input("Player 1, do you choose rock, paper, or scissor? ")
    player2_choice = input("Player 2, do you choose rock, paper, or scissor? ")
    if player1_choice in (rock, paper, scissor) and player2_choice in (rock, paper, scissor):
        break

# Establishes the rules
        # rock
while player1_choice == rock:
    if player2_choice == paper:
        print(player_1, "loses")
        break
    if player2_choice == scissor:
        print(player_2, "loses")
        break
    if player1_choice == player2_choice:
        break
        # paper
while player1_choice == paper:
    if player2_choice == scissor:
        print(player_1, "loses")
        break
    if player2_choice == rock:
        print(player_2, "loses")
        break
    if player1_choice == player2_choice:
        break
        # scissor
while player1_choice == scissor:
    if player2_choice == rock:
        print(player_1, "loses")
        break
    if player2_choice == paper:
        print(player_2, "loses")
        break
    if player1_choice == player2_choice:
        break
        # tie
if player1_choice == player2_choice:
    print("Tie!")
