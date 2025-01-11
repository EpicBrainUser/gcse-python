# game_controller.py
from inventory_manager import InventoryManager    # Import our inventory management class
from menu_system import GameMenu                 # Import our menu system class
from utils import print_with_delay               # Import our custom printing function
import time                                      # Import time module for delays

class GameController:
    """A class to control the main game flow"""
    
    def __init__(self):
        """Constructor method - creates a new GameController instance
        This creates both an InventoryManager and GameMenu when the controller starts
        The 'self' parameter refers to the instance being created"""
        self.inventory_manager = InventoryManager()    # Create inventory management system
        self.menu = GameMenu()                        # Create menu system
        # These become properties of this GameController instance (self)

    def run_game(self):
        """Method to run the main game loop"""
        while True:                                   # Keep running until player quits
            selection = self.menu.display_menu()      # Show menu and get choice
            
            # Handle different menu selections
            if selection == 'A':
                self.inventory_manager.display_items()    # Show inventory
            elif selection == 'B':
                self.inventory_manager.add_item()         # Add item
            elif selection == 'C':
                self.inventory_manager.remove_item()      # Remove item
            elif selection == 'Q':
                print_with_delay("Thanks for playing!")   # Quit game
                time.sleep(1)
                break                                    # Exit the loop
