#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    maxint = 0
    for i in range(len(my_list)):
        if my_list[i] > maxint:
            maxint = my_list[i]
    return maxint
