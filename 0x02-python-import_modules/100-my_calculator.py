#!/usr/bin/python3
import sys
import calculator_1 as calc

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == '+':
        op = calc.add
    elif sys.argv[2] == '-':
        op = calc.sub
    elif sys.argv[2] == '*':
        op = calc.mul
    else:
        op = calc.div
    print("{} {} {} = {}".format(a, sys.argv[2], b, op(a, b)))
