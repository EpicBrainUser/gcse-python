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

def menuCaller():
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
menuCaller()
