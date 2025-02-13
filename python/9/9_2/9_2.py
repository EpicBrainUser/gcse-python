##!/usr/local/bin/python3
from write import append

content=input("Enter the content you wanna write:  ")
file=input("Enter the file you wanna write to:   ")
mode=input("Enter the mode you wanna use:    ")

append(content, file, mode)
