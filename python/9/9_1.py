#!/usr/local/bin/python3

def writeFiles():
    myFile =open('yeah.txt','w')
    myFile.write("hello")
    myFile.write("\n")
    myFile.write("farewell")
    myFile.close()

writeFiles()
