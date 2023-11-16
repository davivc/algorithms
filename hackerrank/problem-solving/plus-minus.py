#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n = len(arr)
    n_pos = 0
    n_zer = 0
    n_neg = 0
    
    for i in arr:
        if i < 0:
            n_neg += 1
        elif i > 0:
            n_pos += 1
        else:
            n_zer += 1
            
    print(f'{(n_pos/n):6f}')
    print(f'{(n_neg/n):6f}')
    print(f'{(n_zer/n):6f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
