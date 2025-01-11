# main.py
from simple_menu import simple_menu          # Import the main menu system
from game_controller import GameController   # Import our game controller
from utils import print_with_delay          # Import our custom printing function
import time                                # Import time module for delays

def main():
    """Main function that runs the game"""
    while True:                            # Keep running until player quits
        user_selection = simple_menu()     # Show main menu and get choice
        
        if user_selection == 'A':
            name = input("What is your name? ")
            print_with_delay(f"Hello {name}, it's good to see you")
            time.sleep(1)
        elif user_selection == 'B':
            print_with_delay("Game is starting...")
            time.sleep(1.5)
            game_controller = GameController()    # Create new game controller
            game_controller.run_game()            # Start the game
        elif user_selection == 'C':
            print_with_delay("Thank you for playing")
            time.sleep(1)
            exit()                               # Exit the program

# This checks if this file is being run directly (not imported)
if __name__ == "__main__":
    main()                                      # Start the program
