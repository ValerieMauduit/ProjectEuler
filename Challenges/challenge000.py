# Challenge #
# Description

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


def my_func(data):
    return data


def run():
    data = 42
    solution = my_func(data)
    print(f'The solution is: {solution}')
    return solution
