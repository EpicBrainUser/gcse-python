#8.6 Exercise: 2D arrays.
#1. Declare a 2D array (or “matrix”) with dimensions 3x3 and enter some values.
#2. Print the entire matrix.
#3. Ask a user to specify a position in the matrix, and correctly return the element at that position
#(example output: “You selected the second list, third item, which is: ____” )

matrix = [[1,2,3], [4,5,6], [7,8,9]]
#print(f"The current matrix is: \n{matrix}")

def users_list_and_position():
    level_1 = int(input("what list do you want?: "))
    level_2 = int(input("what item do you want?: "))
    print(f"You selected this: {matrix[level_1-1][level_2-1]}")

users_list_and_position()
