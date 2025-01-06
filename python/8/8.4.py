#8.4 Exercise: Checking items in a list
#1. Open a new python file as ‘simple_menu’ and copy the code above (both bits). Enter an invalid option to test it works....
#Notice that the menu only works once... so we cannot make another choice in the case of an invalid selection initially.. The solution is to use a loop.
#The program will continue to ask for a choice until one of the three items in the valid_option list has been selected. When “A”, “B” or “C” is entered, the print statement on Line 11 is executed followed by the break statement on Line 12 which stops the WHILE loop.
#Why is a WHILE loop used here and not a FOR loop?
#2. Amend your “simple_menu’’ to run the menu inside a function and return the selection variable.
#3. Use a main( ) function to run the following program:
#a. When A is selected, the program should ask for your name and print a welcome message
#including the user’s name. The menu should then be displayed again.
#b. When B is selected, the program should simply print ‘Game is starting’. The menu should then
#be displayed again. (We will add more functionality here in a bit....!)
#c. When C is selected, the program should print ‘Thank you for playing’ and finish.

def simple_menu():
    print("\t\tGame Menu\n")
    print("\t\tA - Enter Name\n\t\tB - Play Game \n\t\tC - Quit")
    
    valid_option = ['A','B','C']
    
    while True:
        selection = input("Please enter your choice: ").upper()
        if selection in valid_option:
            print("That is a valid choice")
            return selection
#            break
        else:
            print("That is not a valid choice")

def main():
    while True:
        userSelection = simple_menu()
        if userSelection == 'A':
            name = input("What is your name?")
            print(f"Hello {name}, it's good to see you")
        elif userSelection == 'B':
            print("Game is starting...")
        elif userSelection == 'C':
            print("Thank you for playing")
            exit()

#selection = simple_menu()
main()
