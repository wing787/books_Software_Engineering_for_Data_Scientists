import numpy as np
import timeit


random_integers = np.random.randint(1, 1_000_000, 1_000_000)

def slow_way_to_calculate_mode(list_of_integers):
    result_dict= {}
    for i in list_of_integers:
        if i not in result_dict:
            result_dict[i] = 1
        else:
            result_dict[i] += 1

    mode_vals = []
    max_frequency = max(result_dict.values())
    for key, value in result_dict.items():
        if value == max_frequency:
            mode_vals.append(key)

    return mode_vals

mode_timer = timeit.Timer(
    stmt = "slow_way_to_calculate_mode(random_integers)",
    setup = "from __main__ import slow_way_to_calculate_mode, random_integers",
)

time_taken = mode_timer.timeit(number=10)
print(f"Execution time: {time_taken} seconds")