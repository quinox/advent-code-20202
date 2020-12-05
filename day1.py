#!/bin/bash
import sys
found = [False] * 2200
with open(sys.argv[1]) as handle:
    for line in handle:
        number = int(line)
        opposite_number = 2020 - number
        if found[opposite_number]:
            print("{} * {} = {}".format(opposite_number, number, opposite_number * number))
            sys.exit(0)
        found[number] = True
print("No combination found that adds up to 2020.")
sys.exit(1)
