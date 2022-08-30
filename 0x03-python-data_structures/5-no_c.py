#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for character in my_string:
        new_str += character if character != "C" and character != "c" else ""
    return (new_str)
