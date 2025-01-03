# Challenge #2
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
# even-valued terms. (An even number is an integer that can be divided by two.)

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


def fibonacci_sequence(max_value=4000000):
    sequence = [1, 2]
    while sequence[-1] < max_value:
        sequence += [sequence[-1] + sequence[-2]]
    return sequence[:-1]


def sum_even_fibonacci_numbers(max_value=4000000):
    sequence = fibonacci_sequence(max_value)
    return sum(sequence[1::3])


def run():
    solution = sum_even_fibonacci_numbers()
    print(f'The solution is: {solution}')
    return solution
