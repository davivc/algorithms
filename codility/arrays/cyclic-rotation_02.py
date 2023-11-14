from collections import deque

def solution(A, K):
    i = 0
    A_q = deque(A) # O(n)
    while i < K and len(A) > 0: # O(k)
        A_q.appendleft(A_q.pop()) # O(1+1)
        i += 1
    return list(A_q) # O(n)