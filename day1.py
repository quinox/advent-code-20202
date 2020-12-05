#!/bin/bash
import sys

def main():
    desired_sum = 2200
    found = [False] * desired_sum
    with open(sys.argv[1]) as handle:
        for line in handle:
            found_number = int(line)
            if found_number <= 0 or found_number >= desired_sum:
                continue
            opposite_number = desired_sum - found_number
            if found[opposite_number]:
                print("{} * {} = {}".format(opposite_number, number, opposite_number * number))
                sys.exit(0)
            found[found_number] = True
    print("No combination found that adds up to 2020.")
    sys.exit(1)

if __name__ == '__main__':
    main()
