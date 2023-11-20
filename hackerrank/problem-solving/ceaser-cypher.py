#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k): # O(n)

    # Special cases k > 26
    # 66 > 26
    # 66 - 26 - 26 = 14
    if k > 26:
        k = k % 26

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_rot = alpha[k:]+alpha[:k]
    alpha = alpha + alpha.upper()
    alpha_rot = alpha_rot + alpha_rot.upper()
    alpha_hash = {}
    
    for i in range(len(alpha)): # O(n)
        alpha_hash[alpha[i]] = alpha_rot[i]
    print(alpha_hash)
    
    s_arr = [*s]
    for i in range(len(s_arr)): # O(n)
        try:
            letter = s_arr[i]
            s_arr[i] = alpha_hash[letter]
        except:
            continue
        
    return ''.join(s_arr)
        
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
