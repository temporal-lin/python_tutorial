#!/usr/bin/env python3

import os

# print(os.getcwd())

# os.rename("first.txt", "second.txt")

# os.system('ls')

file = input("The file name you want to search: ")

if os.path.isfile(file):
    print("This file exists.")
else:
    print("This file does not exist!")
