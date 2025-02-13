#!/usr/bin/python3

def read(file):
    with open (file, "r") as fileToRead:
        studentsArray = fileToRead.readlines()
        return studentsArray
