# inventory_manager.py
from utils import print_with_delay    # Import our custom printing function
import time                          # Import time module for delays

class InventoryManager:
    """A class to manage the game's inventory system"""
    
    def __init__(self):
        """Constructor method - creates a new InventoryManager instance
        The 'self' parameter refers to the instance being created
        This method runs automatically when creating a new InventoryManager"""
        self.inventory = []          # Create an empty list to store inventory items
                                    # 'self.inventory' means this list belongs to this specific instance

    def add_item(self):
        """Method to add an item to the inventory"""
        item = input("Enter the item name to add: ")     # Get item name from user
        self.inventory.append(item)                      # Add the item to our inventory list
        time.sleep(0.5)                                 # Pause briefly for effect
        print_with_delay(f"{item} has been added to your inventory.")
        time.sleep(1)

    def remove_item(self):
        """Method to remove an item from the inventory"""
        if not self.inventory:           # Check if inventory is empty
            print_with_delay("Your inventory is empty.")
            return                      # Exit the method if inventory is empty
        
        # If we get here, inventory has items
        print_with_delay("Current inventory:")
        time.sleep(0.5)
        
        # Display numbered list of items
        for i, item in enumerate(self.inventory):    # enumerate gives us both index and item
            print_with_delay(f"{i + 1}. {item}", delay=0.05)
        
        # Try/except block handles potential errors when getting user input
        try:
            # Try to execute this code - might cause an error
            choice = int(input("\nEnter the number of the item to remove: ")) - 1
            # Check if choice is valid (within list bounds)
            if 0 <= choice < len(self.inventory):
                removed_item = self.inventory.pop(choice)    # Remove and store the item
                time.sleep(0.5)
                print_with_delay(f"{removed_item} has been removed from your inventory.")
                time.sleep(1)
            else:
                print_with_delay("Invalid item number.")
        except ValueError:
            # This code runs if an error occurred in the try block
            # ValueError happens when int() can't convert the input to a number
            print_with_delay("Please enter a valid number.")

    def display_items(self):
        """Method to display all items in the inventory"""
        if not self.inventory:           # Check if inventory is empty
            print_with_delay("Your inventory is empty.")
            return                      # Exit the method if inventory is empty
        
        print_with_delay("Your inventory contains:", delay=0.05)
        time.sleep(0.5)
        print()                        # Print blank line for spacing
        for item in self.inventory:    # Loop through each item in inventory
            print_with_delay(f"- {item}", delay=0.05)
            time.sleep(0.2)            # Pause between items
        print()                        # Print blank line at end
