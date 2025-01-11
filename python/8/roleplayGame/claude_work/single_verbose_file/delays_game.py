# game.py
from simple_menu import simple_menu
import time
import sys

def print_with_delay(text, delay=0.03):
    """Print text character by character with a specified delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def game():
    inventory = []
    
    def add_item_to_inventory():
        item = input("Enter the item name to add: ")
        inventory.append(item)
        time.sleep(0.5)  # Brief pause before confirmation
        print_with_delay(f"{item} has been added to your inventory.")
        time.sleep(1)  # Pause after confirmation

    def remove_item_from_inventory():
        if not inventory:
            print_with_delay("Your inventory is empty.")
            return
        
        print_with_delay("Current inventory:")
        time.sleep(0.5)
        for i, item in enumerate(inventory):
            print_with_delay(f"{i + 1}. {item}", delay=0.05)
            
        try:
            choice = int(input("\nEnter the number of the item to remove: ")) - 1
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
        if not inventory:
            print_with_delay("Your inventory is empty.")
            return
        
        print_with_delay("Your inventory contains:", delay=0.05)
        time.sleep(0.5)  # Pause before listing items
        print()  # Add blank line for spacing
        for item in inventory:
            print_with_delay(f"- {item}", delay=0.05)
            time.sleep(0.2)  # Short pause between items
        print()  # Add blank line after inventory

    def game_menu():
        print("\n******* Game Menu *******")
        time.sleep(0.3)
        options = [
            "A - Print Inventory Items",
            "B - Add Item To Inventory",
            "C - Remove Item From Inventory",
            "Q - Quit"
        ]
        for option in options:
            print_with_delay(option, delay=0.02)
            time.sleep(0.1)
        
        valid_options = ['A', 'B', 'C', 'Q']
        print()  # Add blank line before input
        selection = input("Please enter your choice: ").upper()
        if selection in valid_options:
            return selection
        else:
            print_with_delay("That is not a valid choice")
            return None

    # Main game loop
    while True:
        player_selection = game_menu()
        
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
    while True:
        user_selection = simple_menu()
        if user_selection == 'A':
            name = input("What is your name? ")
            print_with_delay(f"Hello {name}, it's good to see you")
            time.sleep(1)
        elif user_selection == 'B':
            print_with_delay("Game is starting...")
            time.sleep(1.5)
            game()
        elif user_selection == 'C':
            print_with_delay("Thank you for playing")
            time.sleep(1)
            exit()

if __name__ == "__main__":
    main()
