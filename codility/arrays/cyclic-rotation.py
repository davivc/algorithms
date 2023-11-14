def solution(A, K):
    i = 0
    while i < K and len(A) > 0: # O(k)
        last = A.pop() # O(1)
        A.insert(0, last) # O(n)
        i += 1
    return A