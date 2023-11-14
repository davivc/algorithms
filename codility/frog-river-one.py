def solution(X, A):
    leaves = set([])
    for i in range(len(A)):
        if A[i] not in leaves: 
            leaves.add(A[i])
        
        if len(leaves) == X:
            return i

    return -1