#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a, b = tuple_a
    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            (c,) = tuple_b
            d = 0
        if len(tuple_b) == 0:
            c, d = 0, 0
    elif len(tuple_b) > 2:
        tuple_b = tuple_b[0:2]
        c, d = tuple_b
    else:
        c, d = tuple_b
    result = (a + c, b + d)
    return (result)
