

def game():
    wanna_play = True
    while wanna_play:
        inventory = []
        selected_item = ""
    

        def add_item_to_inventory():
            item = input("Enter the item name to add: ")
            inventory.append(item)
            print(f"{item} has been added to your inventory.")

        def remove_item_from_inventory():
            print_items()
            item_index = input("Enter the number of the item you want to remove: ")
            try:
                item_index = int(item_index) - 1
                if 0 <= item_index < len(inventory):
                    removed_item = inventory.pop(item_index)
                    print(f"You removed {removed_item} from the inventory.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Please enter a valid number.")           
               # remItem = input("Enter the name of the item you want to remove: ")
               # if remItem in inventory:
               #     inventory.remove(remItem)
               # else:
               #     print("Item not found in inventory")
        def view_selected_item():
            # if not selected_item:
            #     print("Nothing selected")
            # else:
            #     print(f"The current selected item is: {selected_item}\n")
            if len(selected_item) == 0:
                print("No selected item")
            else:
                print(f"The current selected item is {selected_item}")
            
  
        def return_selected_item_to_inventory():
            nonlocal selected_item
            item = selected_item
            inventory.append(item)
            selected_item = ""
     
        def get_item_from_inventory():
           nonlocal selected_item
           if selected_item:
               print("You already have an item selected. Return it first.")
           else:
               print_items()
               item_index = input("Enter the number of the item you want to get: ")
               try:
                   item_index = int(item_index) - 1
                   if 0 <= item_index < len(inventory):
                       selected_item = inventory.pop(item_index)
                       print(f"You got {selected_item} from the inventory.")
                   else:
                       print("Invalid item number.")
               except ValueError:
                   print("Please enter a valid number.")           
          
        def quit():
            nonlocal wanna_play
            wanna_play = False
            print("sorry to see you go. ")
    
        def print_items():
            # print(f"Your inventory is: {inventory}")
            # print(list(enumerate(f"Your inventory is: {inventory}")))    
            if not inventory:
                print("Nothing in inventory \n")
            else: 
                print("The current inventory is: \n")
                for i, item in enumerate(inventory, start=1):
                    print(f"{i}. {item}")

        def actual_game_menu():
            print("\t\tActual Game Menu\n")
            # print("\t\tA - Print Inventory Items\n\t\tB - Add Item To Inventory\n\t\tC - Remove Item From Inventory\n\t\tF - Quit")
            print("""
            A - Print Inventory Items
            B - Add Item To Inventory
            C - Remove Item From Inventory
            D - View selected item
            E - Get item from inventory
            F - Return selected item to inventory
            G - Quit""")
            
            valid_option = ['A','B','C', 'D', 'E', 'F', 'G']
            
            while True:
                selection = input("Please enter your choice: ").upper()
                if selection in valid_option:
                    print("That is a valid choice\n\n\n")
                    return selection
                else:
                    print("That is not a valid choice\n\n\n")
        def callEmAll():
            while wanna_play:
                playerSelection = actual_game_menu()

                if playerSelection == 'A':
                    print_items()

                elif playerSelection == 'B':
                    add_item_to_inventory()

                elif playerSelection == 'C':
                    remove_item_from_inventory()

                elif playerSelection == 'D':
                    view_selected_item()

                elif playerSelection == 'E':
                    get_item_from_inventory()

                elif playerSelection == 'F':
                    return_selected_item_to_inventory()

                elif playerSelection == 'G':
                    quit()

                else:
                    print("invalid option\n")

        callEmAll()



