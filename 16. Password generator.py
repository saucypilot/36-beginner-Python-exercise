import secrets

password = ""
length = input("How many characters do you want in your password? ")
if length < 8:
    print("Your password is too short, it must be 8 or more. Try again:\n")