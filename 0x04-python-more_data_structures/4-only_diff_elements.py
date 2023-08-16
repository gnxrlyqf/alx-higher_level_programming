#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    common = set()
    for element in set_1:
        if element not in set_2:
            common.add(element)
    for element in set_2:
        if element not in set_1 and element not in common:
            common.add(element)
    return common
