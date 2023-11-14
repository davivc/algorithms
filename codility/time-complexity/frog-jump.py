# Count minimal number of jumps from position X to Y.

import math
def solution(X, Y, D):
    if X == Y: # O(1)
        return 0

    dist = Y - X # O(1)
    return math.ceil(dist/D) # O(1)