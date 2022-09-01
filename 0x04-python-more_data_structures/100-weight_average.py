#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or all(i is None for i in my_list):
        return 0
    product = sum([a * b for a, b in my_list])
    summ = sum(x for _, x in my_list)
    return product / summ
