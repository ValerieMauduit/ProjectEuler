# Challenge #6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


def square_difference(value):
    if value == 1:
        return 0
    else:
        return square_difference(value - 1) + value * value * (value - 1)


def run():
    solution = square_difference(100)
    print(f'The solution is: {solution}')
    return solution
