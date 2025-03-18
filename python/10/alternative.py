def get_score():
    while True:
        score = input("\nWhat was your score. Enter only digits: ")
        if score.isdigit():
            print("\nValue is digit, check passed\n")
            score = int(score)
            if 0 <= score <= 100:
                print("\nValue in range, check passed\n")
                return score
            else:
                print("Invalid score, please enter a number between 0 and 100")
        else:
            print("\nNot a digit, please re-enter\n")


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
    else:
        print("error occured")


def main():
    test_score = get_score()
    find_grade(test_score)


if __name__ == "__main__":
    main()
