#!/usr/bin/env python3
import sys

position = 0
trees = 0
with open(sys.argv[1]) as handle:
    for line in handle:
        objects = list(line.rstrip('\n'))
        marker = 'O'  # no tree
        if objects[(position) % len(objects)] == '#':
            trees += 1
            marker = 'X'  # tree
        objects[position] = marker
        print(''.join(objects))
        position = (position + 3) % len(objects)
print("Encountered {} trees".format(trees))
