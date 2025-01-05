# Challenge #10
# Find the sum of all the primes below two million.

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from numpy import sqrt


# This method is not very efficient
def sum_of_primes(maximum):
    numbers = [n for n in range(2, maximum + 1)]
    prime_numbers = [numbers[0]]
    while prime_numbers[-1] <= sqrt(maximum):
        numbers = [n for n in numbers if n % prime_numbers[-1] != 0]
        prime_numbers += [numbers[0]]
    return sum(prime_numbers + numbers[1:])


def run():
    solution = sum_of_primes(2000000)
    print(f'The solution is: {solution}')
    return solution
