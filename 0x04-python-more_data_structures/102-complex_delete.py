#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None or a_dictionary is []:
        return None
    new = [k for k in a_dictionary if a_dictionary[k] is value]
    for k in new:
        a_dictionary.pop(k)
    return a_dictionary
