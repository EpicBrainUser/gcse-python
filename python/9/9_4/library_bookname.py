def getNameYear():
    bookName = input("Please enter the book name: ")
    bookYear = input("Now please enter the book year: ")
    return bookName, bookYear

def convertTitle(bookName, bookYear):
    bookLetters = bookName[:3].upper()
    bookNumber = bookYear[2:]
    bookCode = bookLetters + bookNumber
    return bookCode

def writeToFile(bookCode):
    with open ("bookcodes.txt", "a") as f:
        f.write(bookCode)

def main():
    bookName, bookYear = getNameYear()
    bookCode = convertTitle(bookName, bookYear)
    writeToFile(bookCode)

if __name__ == "__main__":
    main()
