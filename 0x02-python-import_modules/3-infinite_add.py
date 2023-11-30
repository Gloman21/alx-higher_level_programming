#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sum = 0
    length = len(argv)
    if length == 1:
        sum = 0
    else:
        for i in range(1, lenght):
            sum += int(argv[i])
    print("{}".format(sum))
