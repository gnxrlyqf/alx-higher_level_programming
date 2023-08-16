#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_string = roman_string + 'F'
    sum = 0
    for i in range(len(roman_string) - 1):
        if getvalue(roman_string[i]) >= getvalue(roman_string[i + 1]):
            sum += getvalue(roman_string[i])
        elif getvalue(roman_string[i]) < getvalue(roman_string[i + 1]):
            sum -= getvalue(roman_string[i])
    return sum

def getvalue(c):
    if c is None:
        return 0
    reference = {
        'F': 0,
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    return reference[c]
