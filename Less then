#establish the list variables
a = []
b = []

#takes user input until user types done
print("Please enter multiple numbers to put on a list:\n(type 'done' when finished)")
while True:
    user_input = input()
    if user_input == "done":
        break
    user_input = int(user_input)
    a.append(user_input)
print(a)

#filter the lists by only appending the numbers that are less/equal then the value the user typed in
def filter():
    filter_num = int(input("Enter a number to filter: "))
    for number in a:
        if number <= filter_num:
            b.append(number)
    print(b)

#will execute filter function when it is typed by the user
filter_input = input("Type 'filter' to filter the list that are less then the number you will enter: ")
if filter_input == "filter":
    filter()
