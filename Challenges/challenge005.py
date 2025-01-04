# Challenge #5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


def update_dict(dictionary, key, value=1):
    if key in dictionary.keys():
        dictionary[key] += value
    else:
        dictionary[key] = value
    return dictionary


def prime_divisors(number):
    result = {1: 1}
    rest = number
    divisor = 2
    while rest > 1:
        while rest % divisor == 0:
            result = update_dict(result, divisor)
            rest = rest // divisor
        divisor += 1
    return result


def minimum_product(to_number):
    all_divisors = {}
    for n in range(1, to_number + 1):
        number_divisors = prime_divisors(n)
        for k in number_divisors.keys():
            if k in all_divisors.keys():
                all_divisors[k] = max([number_divisors[k], all_divisors[k]])
            else:
                all_divisors[k] = number_divisors[k]
    factors = [k ** v for k, v in all_divisors.items()]
    result = 1
    for f in factors:
        result = result * f
    return result


def run():
    solution = minimum_product(20)
    print(f'The solution is: {solution}')
    return solution
