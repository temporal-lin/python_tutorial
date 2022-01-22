#!/usr/bin/env python3

import os

file = input("The file name you want to search: ")

if os.path.isfile(file):
    print("This file exists.")
else:
    print("This file does not exist!")
    print("Creating {} ...".format(file))
    os.system('touch {}'.format(file))
