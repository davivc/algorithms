import math
def solution(A, B, K): # O(1)
    if B == 0:
        return 1

    if K > B:
        return 0

    last = math.floor(B / K)
    first = math.ceil(A / K)-1
    
    return last-first