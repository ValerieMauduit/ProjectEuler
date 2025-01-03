import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Challenges import challenge_template


def test_sets():
    return [
        {
            'number': 1,
            'input': {},
            'expected': []
        },
    ]


def test_it_works(test_data, expected):
    solution = challenge_template.my_func(test_data)
    if solution != expected:
        print(f"Your output is: {solution}")
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def main():
    for test in test_sets():
        print(f"=== Test #{test['number']} ===")
        test_it_works(test['input'], test['expected'])


if __name__ == '__main__':
    main()
