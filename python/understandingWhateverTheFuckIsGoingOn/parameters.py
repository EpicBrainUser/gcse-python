def get_name():
    name=input("enter your name \n>")
    return name

def print_name(name):
    print(f"hello {name}")

def main():
    name = get_name()
    print_name(name)

main()
