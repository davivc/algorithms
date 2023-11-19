#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    ar.sort()
    pairs = 0
    
    pair = ar[0]
    n_pair = 1
    for i in range(1, n):
        # print(ar[i], pair, n_pair, pairs)
        if ar[i] != pair:
            pairs += n_pair//2
            pair = ar[i]
            n_pair = 1
        else:
            n_pair += 1
    
    pairs += n_pair//2
            
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
