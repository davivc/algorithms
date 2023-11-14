# Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.

def solution(A):
    part1 = A[0]
    part2 = sum(A[1:]) # O(n)
    diff = abs(part1-part2)
    
    for i in range(1, len(A)-1): # O(n)
        part1 += A[i]
        part2 -= A[i]
        diff = min(abs(part1-part2), diff) # O(2)

    return diff