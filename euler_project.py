#! /usr/bin/env python
import argparse

from Challenges import (
    challenge_template
)


def main():
    parser = argparse.ArgumentParser(description="Project Euler")
    parser.add_argument("--number", type=int, help="Puzzle Id")
    args = parser.parse_args()

    eval(f'challenge{args.number:03.0f}.run()')


if __name__ == "__main__":
    main()
