#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    n = len(arr)
    if n == 1:
        return 'YES'
        
    sum_left = 0
    sum_right = sum(arr[1:])
    # print(arr)
    for i in range(0, n-1):
        # print(arr[i], sum_left, sum_right)
        if sum_left == sum_right:
            return 'YES'
            
        sum_left += arr[i]
        sum_right -= arr[i+1]
            

    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
