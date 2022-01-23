#!/usr/bin/python3

myfile = input("Select a file: ")
try:
    file = open(myfile, "a")
except FileNotFoundError as e:
    print("The file was not found.")
    print(e)
    exit(1)

movies = ["The Matrix", "Dune", "Interstellar"]

for m in movies:
    file.write(m + "\n")
file.close()
