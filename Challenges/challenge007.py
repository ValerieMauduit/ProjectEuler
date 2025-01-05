# Challenge #7
# What is the 10001st prime number?

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


# This method is not very efficient
def nth_prime_number(position):
    prime_numbers = [2]
    n = 1
    number = prime_numbers[-1] + 1
    while n < position:
        is_prime = True
        p = -1
        while is_prime and (p < len(prime_numbers) - 1):
            p += 1
            if number % prime_numbers[p] == 0:
                is_prime = False
        if is_prime:
            if (n + 1) % 100 == 0:
                print(f'Position {n + 1}: {number}')
            prime_numbers += [number]
            n += 1
        else:
            number += 1
    return prime_numbers[-1]


def run():
    solution = nth_prime_number(10001)
    print(f'The solution is: {solution}')
    return solution
