def solution(A):
    part1 = A[0]
    part2 = sum(A[1:])
    diff = abs(part1-part2)
    
    for i in range(1, len(A)-1):
        part1 += A[i]
        part2 -= A[i]
        diff = min(abs(part1-part2), diff)

    return diff