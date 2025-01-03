#! /usr/bin/env python
import argparse
import sys
sys.path.append("./Challenges")


imports = [f'challenge{n:03.0f}' for n in range(1, 999)]
modules = {}
for x in imports:
    try:
        modules[x] = __import__(x)
        # print(f"Successfully imported {x}.")
    except ImportError:
        error = True
        # print(f"Error importing {x}.")


def main():
    parser = argparse.ArgumentParser(description="Project Euler")
    parser.add_argument("--number", type=int, help="Puzzle Id")
    args = parser.parse_args()

    modules[f'challenge{args.number:03.0f}'].run()


if __name__ == "__main__":
    main()
