#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    weight = 0
    if not my_list:
        return 0
    for i in range(len(my_list)):
        total = total + (my_list[i][0] * my_list[i][1])
        weight = weight + my_list[i][1]
    return total / weight
