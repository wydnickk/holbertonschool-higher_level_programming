#!/usr/bin/python3
def islower(c):
    if type(c) is not str or len(c) != 1:
        return False
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    return False
