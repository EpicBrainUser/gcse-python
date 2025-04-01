def get_student_name() -> str:
    name = input("What is your name? \n").strip()
    return name


def get_teacher_name() -> str:
    teacher_name = input(
        "What is your Computer Science Teacher's name? \n").strip()
    return teacher_name


# def get_marks_old() -> float:
#     marks1 = int(
#         input("What were your marks out of 9 for the last homework task? \n"))
#     marks2 = int(
#         input("What were your marks out of 9 for the last two homework tasks? \n"))
#     marks3 = int(
#         input("What were your marks out of 9 for the last three homework tasks? \n"))
#     marks_avg = (marks1+marks2+marks3)/3
#     return marks_avg


def get_marks() -> float:
    """
    Prompt the user to input marks for three homework tasks and calculate the average.
    Returns:
        float: The average of the three homework marks.
    """
    marks = []
    for i in range(1, 4):
        while True:
            try:
                mark = int(
                    input(f"What were your marks out of 9 for homework task {i}? \n"))
                if 0 <= mark <= 9:
                    marks.append(mark)
                    break
                else:
                    print("Please enter a number between 0 and 9.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    return sum(marks) / len(marks)


def teacher_comment(student_name: str, teacher_name: str, marks_avg: float) -> None:
    if marks_avg >= 8:
        print(
            f"Well done, {student_name}, {teacher_name} is very pleased with your effort")
    elif marks_avg >= 6 < 8:
        print(
            f"A good effort, {student_name}. {teacher_name} thinks you should check your work carefully")
    elif marks_avg <= 5:
        print(
            f"{student_name} this is poor. {teacher_name} has asked you to try harder")
    else:
        print("are you sure about that?")


def main():
    name = get_student_name()
    teacher_name = get_teacher_name()
    marks_avg = get_marks()

    teacher_comment(name, teacher_name, marks_avg)


if __name__ == "__main__":
    main()
