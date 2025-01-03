# Challenge #1
# Find the sum of all the multiples of 3 or 5 below 1000.

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


def sum_of_multiples(max_value, multiples):
    return sum([n for n in range(max_value) if any([n % m == 0 for m in multiples])])


def run():
    solution = sum_of_multiples(1000, [3, 5])
    print(f'The solution is: {solution}')
    return solution
