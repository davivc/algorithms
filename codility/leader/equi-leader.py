# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# [1]
# [2,2,3,2,3,3,3]

def solution(A):
    N = len(A)
    leaders = 0

    if N < 2:
        return leaders

    left_counts = dict()
    for i in range(N):
        number = A[i]
        if number in left_counts:
            left_counts[number] += 1
        else:
            left_counts[number] = 1

    right_counts = dict()
    leader = A[-1]
    for i in range(N-1, -1, -1):
        number = A[i]
        if number in right_counts:
            right_counts[number] += 1
        else:
            right_counts[number] = 1

        left_counts[number] -= 1

        if right_counts[leader] < right_counts[number]:
            leader = number
        
        if right_counts[leader] > (N-i)//2 and left_counts[leader] > i//2:
            leaders += 1

    return leaders