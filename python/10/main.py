# 10. Validation Exercise
# In a simple grading system, a student gets a 9 with over 90%, 8 with over 80%, 7 with over 70%, etc.
#
# Write a program which asks for a grade, and tells the user what grade they got.
# Add validation so that the program only accepts digits (doesn’t crash with strings) and valid percentages.
#
# Use a function to “get_test_score()” which returns a value but does not print the grade.
# Declare a variable e.g. “test_score” as you call the function and output the grade.
#
# Ensure that the user cannot continue until a valid value has been entered.
# Output a suitable message if a value does not meet format or range criteria.

# from sys import stdout
"""
def get_score():
    while True:
        print("What was your score. Enter only the digits of the percent: ", end="")
        stdout.flush()
        try:
            user_input = input()
            score = float(user_input)
        #    print(f"\rWhat was your score. Enter only the digits of the percent: {user_input}%")
            break
        except ValueError:
            print("\rPlease enter a valid numeric input: ", end="")
            stdout.flush()
    return score
"""


def get_score():
    while True:
        try:
            score = float(
                input("What was your score. Enter only the digits of the percent: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score, please enter a number between 0 and 100")
        except ValueError:
            print("Invalid input")


def find_grade(test_score):
    if test_score == 100:
        print("You got a 9! Well done on the 100 %")
    elif test_score >= 90:
        print("You got a 9")
    elif test_score >= 80:
        print("You got a 8")
    elif test_score >= 70:
        print("You got a 7")
    elif test_score >= 60:
        print("You got a 6")
    elif test_score >= 50:
        print("You got a 5")
    elif test_score < 50:
        print("failure")


def main():
    test_score = get_score()
    find_grade(test_score)


if __name__ == "__main__":
    main()
