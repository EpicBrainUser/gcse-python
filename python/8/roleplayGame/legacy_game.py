#8.5 Exercise: Role-play game inventory management.
#Role-play games are very popular and often involve moving around a location, solving puzzles and collecting items in your inventory.. These items can then be stored to use later to help you in the game.
#Now add some functionality to the “Play game” option so that you can manage an inventory for the game. Your program must:
#a. be able to add items to your inventory by choosing that option from the menu
#b. be able to display all the items you have in the inventory by choosing that option from the
#menu
#c. allow you to ‘get’ an item from the inventory (this means it is no longer in the inventory) by
#choosing that option from the menu
#d. display the menu again after each choice until you enter ‘q’
#Example:
#******* Options Menu *******
#Enter 'p' to print inventory
#Enter 'a' to print inventory
#Enter 'g' to get an item
#Enter 'q' to quit
#Please enter your choice: >>
#Ideally you will use separate functions for each option, passing the updated inventory between the functions.

import simple_menu.py


def game():
    wanna_play = True
    while wanna_play:
        inventory = []
    
        def add_items_to_menu():
            print("This option isn't developed yet")
        def remove_item_from_inventory():
            print("This option isn't developed yet")
    #   def get_item_from_inventory():
    #   def view_selected_item():
    #   def add_current_item_to_inventory():
        
        def quit():
            print("sorry to see you go. ")
            wanna_play = False
    
        def print_items():
            print(f"Your inventory is: {inventory}")
    
        def actual_game_menu():
            print("\t\tActual Game Menu\n")
            print("\t\tA - Print Inventory Items\n\t\tB - Add Item To Inventory\n\t\tC - Remove Item From Inventory\n\t\tF - Quit")
            
            valid_option = ['A','B','C', 'D', 'E', 'F']
            
            while True:
                selection = input("Please enter your choice: ").upper()
                if selection in valid_option:
                    print("That is a valid choice")
                    return selection
        #            break
                else:
                    print("That is not a valid choice")
        def callEmAll():
            while True:
                playerSelection = actual_game_menu()

            if playerSelection == 'A':
                print_items()

            elif playerSelection == 'B':
                print("This option isn't developed yet")

            elif playerSelection == 'C':
                print("This option isn't developed yet")

            elif playerSelection == 'D':
                print("This option isn't developed yet")

            elif playerSelection == 'E':
                print("This option isn't developed yet")

            elif playerSelection == 'F':
                quit()




simple_menu.simple_menu

#simple_menu.menuCaller

def main():
    while True:
        userSelection = simple_menu()
        if userSelection == 'A':
            name = input("What is your name?")
            print(f"Hello {name}, it's good to see you")
        elif userSelection == 'B':
            print("Game is starting...")
            game()
        elif userSelection == 'C':
            print("Thank you for playing")
            exit()

selection = simple_menu()

main()

'''
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
'''
