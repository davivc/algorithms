# Find the earliest time when a frog can jump to the other side of a river.

def solution(X, A):
    leaves = set([]) # O(1)
    for i in range(len(A)): # O(n)
        if A[i] not in leaves: # O(X) 
            leaves.add(A[i]) # O(1)
        
        if len(leaves) == X:
            return i

    return -1