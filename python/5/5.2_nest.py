def number_ask():
    c_number = int(input("Please enter a number between 1 and 20 \n"))
    return number
number = number_ask()
if number >= 1:
    if number < 20:
        print("output number in correct range. proceed")

else:
    print("number isn't in range. please try again")
    number_ask()

