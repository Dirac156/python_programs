#! /usr/bin/env python3

import sys
import time

def change_o_to_a(str):

    """
    This function takes a string as argument
    It changes every o to a and return a new string.
    """
    lst = [] # list that will hold all letters.
    if not str or type(str) == int:
        sys.exit()
    else:
        for letter in str:
            if letter == "o":
                letter = "a"
            elif letter == "O":
                letter == "A"
            lst.append(letter)
        new_str = ''.join(lst)

    return new_str

user_string = "Dora"
print(change_o_to_a(user_string))
time.sleep(5)
print(change_o_to_a("Hello word"))
print(change_o_to_a(12345))
print(change_o_to_a(0))
