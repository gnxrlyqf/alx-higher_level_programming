#!/usr/bin/python3
import sys
if __name__ == "__main__":
    result = 0
    sys.argv.pop(0)
    for i in sys.argv:
        result += int(i)
    print(result)