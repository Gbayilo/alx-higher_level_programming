#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list or not all(isinstance(tup, tuple) and len(tup) == 2 for tup in my_list):
        return 0

    total_weighted_sum = sum(weight * value for weight, value in my_list)
    total_weights = sum(weight for weight, _ in my_list)

    if total_weights == 0:
        return 0

    return total_weighted_sum / total_weights
