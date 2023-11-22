#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.


def sumXor(n):
    # special case: 0
    if n == 0:
        return 1
        
    n_bits = list(f'{n:b}')
    # print(n_bits)
      
    counter = 0
    for i in n_bits:
        if i == '0':
            counter += 1
    
    return 2**counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
