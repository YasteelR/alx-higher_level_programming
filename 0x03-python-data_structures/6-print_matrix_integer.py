#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    temp = ""
    for elm in matrix:
        for i in elm:
            temp = temp + str(i) + " "  
        print ("{:s}".format(temp))
        temp = ""
