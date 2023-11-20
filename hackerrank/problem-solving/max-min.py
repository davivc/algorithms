#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

# k =
# [ 0,1,2,3 ]

def maxMin(k, arr):
    arr.sort() # O(n log n)
    n = len(arr)
    
    min_unfairness = 10e9
    
    for i in range(n-k+1):
        arr_unfairness = arr[i+k-1] - arr[i]
        min_unfairness = min(min_unfairness, arr_unfairness)
        
    return min_unfairness
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
