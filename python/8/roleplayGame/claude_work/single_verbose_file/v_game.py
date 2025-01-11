# Imports required functionality
from simple_menu import simple_menu  # Imports the menu system
import time   # Used for creating delays
import sys    # Used for character-by-character printing

def print_with_delay(text, delay=0.03):
    """Prints text character by character with a specified delay"""
    # Loops through each character in the provided text
    for char in text:
        # Writes single character without line break
        sys.stdout.write(char)
        # Forces the output to display immediately
        sys.stdout.flush()
        # Pauses briefly between characters
        time.sleep(delay)
    # Adds final line break after text complete
    print()

def game():
    # Creates empty inventory list to store items
    inventory = []
    
    def add_item_to_inventory():
        # Gets item name from user
        item = input("Enter the item name to add: ")
        # Adds new item to inventory list
        inventory.append(item)
        # Brief pause for better user experience
        time.sleep(0.5)
        # Confirms addition with animated text
        print_with_delay(f"{item} has been added to your inventory.")
        time.sleep(1)

    def remove_item_from_inventory():
        # Checks if inventory is empty
        if not inventory:
            print_with_delay("Your inventory is empty.")
            return
        
        # Shows current inventory contents
        print_with_delay("Current inventory:")
        time.sleep(0.5)
        # Lists each item with number for selection
        for i, item in enumerate(inventory):
            print_with_delay(f"{i + 1}. {item}", delay=0.05)
            
        try:
            # Gets user choice of item to remove
            choice = int(input("\nEnter the number of the item to remove: ")) - 1
            # Validates choice and removes item if valid
            if 0 <= choice < len(inventory):
                removed_item = inventory.pop(choice)
                time.sleep(0.5)
                print_with_delay(f"{removed_item} has been removed from your inventory.")
                time.sleep(1)
            else:
                print_with_delay("Invalid item number.")
        except ValueError:
            print_with_delay("Please enter a valid number.")

    def print_items():
        # Checks if inventory is empty
        if not inventory:
            print_with_delay("Your inventory is empty.")
            return
        
        # Displays inventory contents with animation
        print_with_delay("Your inventory contains:", delay=0.05)
        time.sleep(0.5)
        print()
        for item in inventory:
            print_with_delay(f"- {item}", delay=0.05)
            time.sleep(0.2)
        print()

    def game_menu():
        # Displays game menu header
        print("\n******* Game Menu *******")
        time.sleep(0.3)
        
        # Defines menu options
        options = [
            "A - Print Inventory Items",
            "B - Add Item To Inventory",
            "C - Remove Item From Inventory",
            "Q - Quit"
        ]
        
        # Displays each option with animation
        for option in options:
            print_with_delay(option, delay=0.02)
            time.sleep(0.1)
        
        # Defines valid menu choices
        valid_options = ['A', 'B', 'C', 'Q']
        print()
        
        # Gets and validates user selection
        selection = input("Please enter your choice: ").upper()
        if selection in valid_options:
            return selection
        else:
            print_with_delay("That is not a valid choice")
            return None

    # Main game loop - continues until player quits
    while True:
        player_selection = game_menu()
        
        # Handles each menu choice
        if player_selection == 'A':
            print_items()
        elif player_selection == 'B':
            add_item_to_inventory()
        elif player_selection == 'C':
            remove_item_from_inventory()
        elif player_selection == 'Q':
            print_with_delay("Thanks for playing!")
            time.sleep(1)
            break

def main():
    # Main program loop - continues until player quits
    while True:
        # Gets selection from main menu
        user_selection = simple_menu()
        
        # Handles main menu choices
        if user_selection == 'A':
            name = input("What is your name? ")
            print_with_delay(f"Hello {name}, it's good to see you")
            time.sleep(1)
        elif user_selection == 'B':
            print_with_delay("Game is starting...")
            time.sleep(1.5)
            game()  # Launches the inventory management game
        elif user_selection == 'C':
            print_with_delay("Thank you for playing")
            time.sleep(1)
            exit()

# Ensures main() only runs if this file is run directly
if __name__ == "__main__":
    main()
