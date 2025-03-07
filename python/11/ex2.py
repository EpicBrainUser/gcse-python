def read():
        try:
            with open("file", "r") as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print("file not found")

def printContent():
    content = read()
    print(f"The content of the file is {content}")

def main():
    printContent()

if __name__ == "__main__":
    main()

