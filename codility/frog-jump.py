import math
def solution(X, Y, D):
    if X == Y:
        return 0

    dist = Y - X
    return math.ceil(dist/D)