# game.py
from simple_menu import simple_menu

def game():
    inventory = []
    
    def add_item_to_inventory():
        item = input("Enter the item name to add: ")
        inventory.append(item)
        print(f"{item} has been added to your inventory.")

    def remove_item_from_inventory():
        if not inventory:
            print("Your inventory is empty.")
            return
        
        print("Current inventory:")
        for i, item in enumerate(inventory):
            print(f"{i + 1}. {item}")
            
        try:
            choice = int(input("Enter the number of the item to remove: ")) - 1
            if 0 <= choice < len(inventory):
                removed_item = inventory.pop(choice)
                print(f"{removed_item} has been removed from your inventory.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")

    def print_items():
        if not inventory:
            print("Your inventory is empty.")
        else:
            print("Your inventory contains:")
            for item in inventory:
                print(f"- {item}")

    def game_menu():
        print("\n******* Game Menu *******")
        print("A - Print Inventory Items")
        print("B - Add Item To Inventory")
        print("C - Remove Item From Inventory")
        print("Q - Quit")
        
        valid_options = ['A', 'B', 'C', 'Q']
        
        selection = input("Please enter your choice: ").upper()
        if selection in valid_options:
            return selection
        else:
            print("That is not a valid choice")
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
            print("Thanks for playing!")
            break

def main():
    while True:
        user_selection = simple_menu()
        if user_selection == 'A':
            name = input("What is your name? ")
            print(f"Hello {name}, it's good to see you")
        elif user_selection == 'B':
            print("Game is starting...")
            game()
        elif user_selection == 'C':
            print("Thank you for playing")
            exit()

if __name__ == "__main__":
    main()
