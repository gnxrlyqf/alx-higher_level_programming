#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            y += 1
        except:
            print()
            return y
    print()
    return y