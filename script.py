#!/usr/bin/env python3

def my_function():
    """This is just a comment
    How are these numbers gonna add up?
    """
    mynum1 = 50
    mynum2 = 20
    print(mynum1 + mynum2)

my_function()

def sec_function():
    global msg
    msg = "Hello everyone!"
    print(msg)

sec_function()

print(msg)
