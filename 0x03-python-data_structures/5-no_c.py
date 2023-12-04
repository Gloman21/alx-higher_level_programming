#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    if my_string is None:
        return None
    for elements in my_string:
        if elements == "c" or elements == "C":
        else:
            new_string += elements
    return new_string
