def get_student():
    name = input("What is your name? \n")
    return name
def cs_name():
    c_name = input("What is your Computer Science Teacher's name? \n")
    return c_name

def get_marks():
    marks1 = int(input("What were your marks out of 9 for the last homework task? \n"))
    marks2 = int(input("What were your marks out of 9 for the last two homework tasks? \n"))
    marks3 = int(input("What were your marks out of 9 for the last three homework tasks? \n"))
    marks_avg = (marks1+marks2+marks3)/3
    return marks_avg
def teacher_comment(name, c_name, marks_avg):
    if marks_avg >=8:
        print(f"Well done, {name}, {c_name} is very pleased with your effort")
    elif marks_avg >= 6 < 8:
        print(f"A good effort, {name}. {c_name} thinks you should check your work carefully")
    elif marks_avg <=5:
        print(f"{name} this is poor. {c_name} has asked you to try harder")
    else:
        print("are you sure about that?")

name = get_student()
c_name = cs_name()
marks_avg = get_marks()
teacher_comment(name, c_name, marks_avg)

