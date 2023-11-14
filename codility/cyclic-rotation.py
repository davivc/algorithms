def solution(A, K):
    i = 0
    while i < K and len(A) > 0:
        last = A.pop()
        A.insert(0, last)
        i += 1
    return A