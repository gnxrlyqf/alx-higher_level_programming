#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        print(test)
    except NameError as ex:
        raise NameError(message) from ex
