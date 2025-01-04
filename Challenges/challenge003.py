# Challenge #3
# What is the largest prime factor of the number 600851475143?

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


def get_max_prime_factor(number):
    rest = number
    factor = 2
    while factor < rest:
        if rest % factor == 0:
            rest = rest // factor
        else:
            factor += 1
    return rest


def run():
    solution = get_max_prime_factor(600851475143)
    print(f'The solution is: {solution}')
    return solution
