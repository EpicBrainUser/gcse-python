#9.3 Exercise: Reading from files
#1.	Create a text file with the first names of the students in your class and save it as ‘students.txt’.  Read the file into a list
#        Sort the list into alphabetical order (list.sort() will do it!)
#        Print out the list items on separate lines (with no extra return characters... as above!)

# import sys
from write import write
from read import read
from sort import sort
from neat_print import neat_print


def collect_names():

    file = input("""
       What's the name of the file you want to write the students' names to? 
       hint: type exit to end collecting names""")

    print("Enter names: ")
    names = []

    while True:
        name = input("Enter a name: ")
        if name.lower() == "exit":
            break
        names.append(name)

    for name in names:
        print(f"- {name}")

    write(names, file)

    return file


def main():
    # file = collect_names()
    # studentsArray = read(file)
    # sortedStudentsArray = sort(studentsArray)
    # neat_print(sortedStudentsArray)
    neat_print(sort((read(collect_names()))))


if __name__ == "__main__":
    main()
