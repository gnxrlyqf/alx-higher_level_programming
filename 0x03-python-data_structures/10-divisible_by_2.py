#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    output_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            output_list.append(True)
        else:
            output_list.append(False)
    return output_list
