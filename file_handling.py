#!/usr/bin/env python3

myfile = input("Select a file: ")

try:
    file = open(myfile, "r")
except FileNotFoundError as e:
    print("File was not found!")
    print(e)
    exit(1)

for line in file:
    print(line)
