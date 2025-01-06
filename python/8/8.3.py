#8.3 Exercise: List practice
#Ask a user to enter numbers until they enter 0.
#Add the numbers into a list (you will need to declare an empty list to append into). Sort the numbers into order and print the sorted list.numbers = []
numbers = []
while True:
    user = int(input("Enter a number.\n"))
    if user == 0:
        break
    else:
        numbers.append(input)

numbers.sort()
print(f"The ordered list is {numbers}")
