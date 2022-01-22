#!/usr/bin/env python3

foods = ("Lasagna", "Pizza", "Burger")

try:
    foods[1] = "American Pizza"
except:
    print("There was an error!")

print(foods)
