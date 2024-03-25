#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        a, b = 0, 0
    elif len(tuple_a) == 1:
        (a,) = tuple_a
        b = 0
    else:
        a, b = tuple_a

    if len(tuple_b) == 0:
        c, d = 0, 0
    elif len(tuple_b) == 1:
        (c,) = tuple_b
        d = 0
    else:
        c, d = tuple_b

    return (a + c, b + d)
