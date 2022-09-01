#!/usr/bin/python3
def helper(i):
    if i is "I":
        return 1
    elif i is "V":
        return 5
    elif i is "X":
        return 10
    elif i is "L":
        return 50
    elif i is "C":
        return 100
    elif i is "D":
        return 500
    elif i is "M":
        return 1000
    else:
        return 0


def roman_to_int(roman_string):
    count = 0
    future = 0
    number = 0

    if type(roman_string) is not str or roman_string is None:
        return 0
    if len(roman_string) is 1:
        return helper(roman_string[0])
    for i in range(0, len(roman_string) - 1):
        number = helper(roman_string[i])
        future = helper(roman_string[i + 1])
        if number >= future:
            count += number
        elif number < future:
            count -= number
    count += future
    return count
