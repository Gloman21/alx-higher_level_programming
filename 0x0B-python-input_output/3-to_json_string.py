#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    representation = json.dumps(my_obj)
    return representation
