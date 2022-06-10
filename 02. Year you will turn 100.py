input("What is your name? ")
print("Nice name")
age = int(input("What is your age? "))
until_hundred = 100 - age

#Uses the datetime module to get current year
import datetime
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
the_year = int(year) + until_hundred
print(the_year)
