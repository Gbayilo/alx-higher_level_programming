#!/usr/bin/python3

def islower(c):
    '''
    This function checks for a lowercase character

    Returns:
    True if lowercase and False otherwise
    '''

    if ord(c) in range(97, 123):
        return True
    else:
        return False
