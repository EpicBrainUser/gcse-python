def getCode():
    bookName = input("Please enter the book name: ")[:3].upper()
    while True:
        bookYear = input("Now please enter the book year: ")[-2:].upper()
        if bookYear.isdigit():
            break
        else:
            print("\nBook year must be all digits\n")
    bookCode = bookName + bookYear
    return bookCode

def writeToFile(bookCode):
    with open ("bookcodes.txt", "a") as f:
        f.write(f"{bookCode}\n")

def main():
    bookCode = getCode()
    # bookCode = convertTitle(bookName, bookYear)
    writeToFile(bookCode)

if __name__ == "__main__":
    main()
