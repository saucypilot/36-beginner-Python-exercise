import random
# Creates the lists
a = []
b = []
c = []

# Asks user how many numbers they want for both lists
listA = int(input("How many numbers would you like on list a? "))
listB = int(input("How many numbers would you like on list b? "))

# Function that randomly generates numbers for the lists
def listgenerator(list): 
    while len(a) < list :
        number_generator = a.append(random.randint(0,10))
    print("a = ", a)

def list2generator(list):
    while len(b) < list :
        number_generator = b.append(random.randint(0,10))
    print("b = ", b)

# Function call
listgenerator(listA)
list2generator(listB)

# List comprehension
c = [number for number in a if number in b]
print("Both lists contain the numbers: ", c)
