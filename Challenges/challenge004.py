# Challenge #4
# Find the largest palindrome made from the product of two 3-digit numbers.

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from numpy import sqrt


def is_palindrome(number):
    str_number = str(number)
    middle = int(len(str_number) / 2)
    return all([str_number[i] == str_number[-(i + 1)] for i in range(middle)])


def largest_palindrome_product(digits=3):
    max_number = int('9' * digits)
    max_product = max_number * max_number
    found = False
    number = max_product + 1
    while not found:
        number -= 1
        if is_palindrome(number):
            split_divisor = int(sqrt(number))
            divisor = int('9' * digits)
            while (number % divisor != 0) and (divisor >= split_divisor):
                divisor -= 1
            if number % divisor == 0:
                print('   ' + str(divisor))
                found = True
    return number


def run():
    solution = largest_palindrome_product(3)
    print(f'The solution is: {solution}')
    return solution
