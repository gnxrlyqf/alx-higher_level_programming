#!/usr/bin/python3
def print_last_digit(number):
    print("{}".format(number % 10 if number >= 0 else (-number) % 10))
