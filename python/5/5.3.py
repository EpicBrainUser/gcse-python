def askNumber():
    base = int(input("Enter a number between 1 and 12\n>>>"))
    while base < 1 or base > 12:
        base = int(input("That number is out of range, please re-enter the number\n>>>"))
    return base

def calculate():
    for x in range(10):
        print((x+1)*base)
        x+=1

base = askNumber()
calculate()

