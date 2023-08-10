#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sys.argv.pop(0)
    args = "arguments" if len(sys.argv) != 1 else "argument"
    end = "." if len(sys.argv) == 0 else ":"
    print("{} {}{}".format(len(sys.argv), args, end))
    for i in range (len(sys.argv)):
        print("{}: {}".format(i + 1, sys.argv[i]))
