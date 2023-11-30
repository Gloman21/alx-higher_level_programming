#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    list_names = dir(hidden_4)
    list_names.sort()
    for text in list_names:
        if "__" not in text:
            print("{}".format(text))
