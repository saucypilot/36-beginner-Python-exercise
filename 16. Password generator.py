import secrets

#Variables I will need
password = ""
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!#@$%&()[{]}"
numbers = "01234556789"

#Prompt the user for the passwored length
length = input("How many characters do you want in your password? ")
if length < 8:
    while True:
        length = input("Your password is too short, it must be 8 or more. Try again:\n")
        if length >= 8:
            break

for 