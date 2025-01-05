# Challenge #9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a² + b² = c²
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from numpy import sqrt


def pythagorean_triplet(triplet_sum):
    b = int(triplet_sum / 2)
    a = b - 1
    c = sqrt(a ** 2 + b ** 2)
    while (a + b + c != triplet_sum) and (b > 1):
        if a > 1:
            a -= 1
            c = sqrt(a ** 2 + b ** 2)
        else:
            b -= 1
            a = b - 1
            c = sqrt(a ** 2 + b ** 2)
    if b == 1:
        return None
    print([a, b, c])
    print([a ** 2, b ** 2, c ** 2])
    return int(a * b * c)


def run():
    solution = pythagorean_triplet(1000)
    print(f'The solution is: {solution}')
    return solution
