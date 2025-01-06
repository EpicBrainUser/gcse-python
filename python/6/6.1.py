#6.1 Exercise: Using Date and Time
#Write a program that will display the day of the week that a user was born on....
#- Use functions if you can, to ask for the date, month and year (as integers).
#- Display the date to the user in this format: 15/Jan/97, and tell them what day of the week they were born on.

import time
import datetime

def getDateBorn():
    dayBorn = int(input("What day were you born on?\n"))
    weekBorn = int(input("What month were you born on \n btw enter an integer for the number out of the year. \n"))
    yearBorn = int(input("What year were you born on? \n"))
    return dayBorn, weekBorn, yearBorn


def printGivenDate(day,month,year):
    birthday = datetime.date(year, month, day)
    print(f"You were born on {birthday.strftime('%A')}")

day, month, year = getDateBorn()
printGivenDate(day,month,year)
