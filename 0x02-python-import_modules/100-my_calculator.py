#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argv = sys.argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if operator == '+':
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    elif operator == '-':
        print ("{} {} {} = {}".format(a, operator, b, sub(a, b)))
    elif operator == '*':
         print ("{} {} {} = {}".format(a, operator, b, mul(a, b)))
    elif operator == '/':
        if b == 0:
            print("Error: Division by zero")
            sys.exit(1)
        print ("{} {} {} = {}".format(a, operator, b, div(a, b)))
    else:
        print("Unkown operator. Available operators: +, -, * and /")
        sys.exit(1)
