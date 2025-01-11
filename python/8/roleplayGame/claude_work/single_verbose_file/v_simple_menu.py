def simple_menu():
    # Prints the main game menu header with extra spacing for readability
    print("\t\tGame Menu\n")
    
    # Displays the three main options available to players
    print("\t\tA - Enter Name\n\t\tB - Play Game \n\t\tC - Quit")
    
    # Defines valid menu choices - used to validate user input
    valid_option = ['A','B','C']
    
    # Continuous loop that keeps asking for input until valid option received
    while True:
        # Gets user input and converts to uppercase for consistency
        selection = input("Please enter your choice: ").upper()
        
        # Checks if selection is valid and returns it if so
        if selection in valid_option:
            print("That is a valid choice")
            return selection
        # If invalid, loop continues and asks again
        else:
            print("That is not a valid choice")
