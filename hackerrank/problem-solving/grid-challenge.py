#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Sort all words
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
        
    # Transpose
    grid_t = list(map(list, zip(*grid)))
    
    # Check is all rows are sorted
    for i in range(len(grid_t)):
        if sorted(grid_t[i]) != grid_t[i]:
            return "NO"
    return "YES"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
