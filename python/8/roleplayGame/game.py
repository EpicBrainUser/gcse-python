# 8.5 Exercise: Role-play game inventory management.
# Role-play games are very popular and often involve moving around a location, solving puzzles and collecting items in your inventory.. These items can then be stored to use later to help you in the game.
# Now add some functionality to the “Play game” option so that you can manage an inventory for the game. Your program must:
# a. be able to add items to your inventory by choosing that option from the menu
# b. be able to display all the items you have in the inventory by choosing that option from the
# menu
# c. allow you to ‘get’ an item from the inventory (this means it is no longer in the inventory) by
# choosing that option from the menu
# d. display the menu again after each choice until you enter ‘q’
# Example:
# ******* Options Menu *******
# Enter 'p' to print inventory
# Enter 'a' to print inventory
# Enter 'g' to get an item
# Enter 'q' to quit
# Please enter your choice: >>
# Ideally you will use separate functions for each option, passing the updated inventory between the functions.

from simple_menu import menuCaller
from game_func import game

if __name__ == "__main__":
    menuCaller(game)
