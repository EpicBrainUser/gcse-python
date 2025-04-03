# 8.8 Exercise: Using a loop to add into a 2D array.
# An 11 year old wants a program which will ask for the names of 5 friends to invite to her party and ask the food they will bring. The program will add the names and food items to a 2D list. At the end it will print the entire matrix as neatly as possible! Try:
# 1. Declare an empty party_list
# 2. Use a loop to ask for 5 names and 5 items
# 3. In the loop, create a list containing the name and item, and then append that list to the
# main party_list
# 4. Print final party list



def getNamesAndItems():

    party_list = []

    # count = 1
    for i in range(5):
        # name = input(f"Please enter the name of person {i}: ")
        instance = []
        instance.append(input(f"Please enter the name of person {i + 1}: "))
        # food = input("\nPlease enter the food they will bring: ")
        instance.append(input("\nPlease enter the food they will bring: "))
        party_list.append(instance)
        # count += 1
    return party_list


def printList(party_list):
    print("The full party list is: \n\n")
    print(*party_list, sep="\n")


def main():
    printList(getNamesAndItems())


if __name__ == "__main__":
    main()
