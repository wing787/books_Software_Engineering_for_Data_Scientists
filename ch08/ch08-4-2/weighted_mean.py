import numpy as np


def weighted_mean(num_lst, weights_lst):
    try:
        return np.average(num_lst, weights=weights_lst)
    except ZeroDivisionError:
        return None