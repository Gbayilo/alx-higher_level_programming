#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    while len(my_list) > 1:
        my_list = [
                my_list[i]
                for i in range(len(my_list) - 1)
                if my_list[i] >= my_list[i + 1]
                ]
    return my_list[0]
