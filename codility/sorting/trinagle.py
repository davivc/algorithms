# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# A[R] < A[P]+A[Q]
# A[R] > A[P]-A[Q]
# A[R] > A[Q]-A[P]
# (3, 1, 2, 4,  0,  5]
# [1, 2, 5, 8, 10, 20]
# 10 < 8+5 | 10 > 8-5 | 10 > 5-8
# 20 < 10+8 | 10 > 8-5 | 10 > 5-8


def solution(A):
    # Implement your solution here
    A.sort()
    A.reverse()

    for i in range(len(A)-2):
        R = A[i] 
        Q = A[i+1] 
        P = A[i+2] 
        if R < Q+P and R > P-Q and R > Q-P:
            return 1

    return 0