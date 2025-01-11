# menu_system.py
from utils import print_with_delay    # Import our custom printing function
import time                          # Import time module for delays

class GameMenu:
    """A class to manage the game's menu system"""
    
    def __init__(self):
        """Constructor method - creates a new GameMenu instance
        The 'self' parameter refers to the instance being created
        This method runs automatically when creating a new GameMenu"""
        self.valid_options = ['A', 'B', 'C', 'Q']    # List of valid menu choices
        self.options = [                             # List of menu options to display
            "A - Print Inventory Items",
            "B - Add Item To Inventory",
            "C - Remove Item From Inventory",
            "Q - Quit"
        ]

    def display_menu(self):
        """Method to display the menu and get user selection"""
        print("\n******* Game Menu *******")
        time.sleep(0.3)
        
        # Display each menu option with animation
        for option in self.options:                  # Loop through each menu option
            print_with_delay(option, delay=0.02)     # Print option with slight delay
            time.sleep(0.1)                         # Pause between options
        
        print()                                     # Print blank line for spacing
        # Get and validate user input
        selection = input("Please enter your choice: ").upper()
        
        if selection in self.valid_options:         # Check if selection is valid
            return selection                        # Return valid selection
        else:
            print_with_delay("That is not a valid choice")
            return None                            # Return None for invalid selection
