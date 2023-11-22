#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    if n == 1:
        return 'Richard'
        
    turn = 0
    counter = int(math.log2(n))
    while counter > 1:
        if n > 2**counter:
            n = n - 2**counter
        else:
            n = n/2
        
        if n == 1:
            break
            
        counter = int(math.log2(n))
        turn ^= 1
        
        
        
    
    if turn == 0:
        return 'Louise'
    return 'Richard'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
