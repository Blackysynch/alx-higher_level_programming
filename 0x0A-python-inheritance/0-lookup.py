#!/usr/bin/python3
'''A module for inspecting an object.
'''


def lookup(obj):
    '''Find list of available attributes and methods of the object.

    Args:
        obj (any): A given object.

    Returns:
        list: A list of available attributes and methods the object has.
    '''
    return dir(obj)
