def get_score():
    while True:
        try:
            score = float(
                input("What was your score. Enter only digits: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score, please enter a number between 0 and 100")
        except ValueError:
            print("Invalid input")


def find_grade(test_score):
    grade_ranges = {
        (90, 100): "You got a 9",
        (80, 89): "You got an 8",
        (70, 79): "You got a 7",
        (60, 69): "You got a 6",
        (50, 59): "You got a 5",
        (0, 49): "failure"
    }

    for (lower, upper), message in grade_ranges.items():
        if lower <= test_score <= upper:
            print(message)
            break

    if test_score == 100:
        print("Well done on the 100%!")

# def find_grade(test_score):
#     if test_score == 100:
#         print("You got a 9! Well done on the 100 %")
#     elif test_score >= 90:
#         print("You got a 9")
#     elif test_score >= 80:
#         print("You got a 8")
#     elif test_score >= 70:
#         print("You got a 7")
#     elif test_score >= 60:
#         print("You got a 6")
#     elif test_score >= 50:
#         print("You got a 5")
#     elif test_score < 50:
#         print("failure")


def main():
    test_score = get_score()
    find_grade(test_score)


if __name__ == "__main__":
    main()
