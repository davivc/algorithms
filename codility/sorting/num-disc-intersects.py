# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    n = len(A)
    intersects = 0
    starts = [0]*n
    ends = [0]*n

    for i in range(len(A)):
        s = i - A[i] if i > A[i] else 0
        e = i + A[i] if n-1-i > A[i] else n-1

        starts[s] += 1
        ends[e] += 1

    # print(starts, ends)
    active = 0
    for i in range(len(A)):
        # print(i, intersects, starts[i], ends[i], active, active * starts[i], starts[i] * (starts[i] - 1) // 2)
        intersects += active * starts[i]
        intersects += starts[i] * (starts[i] - 1) // 2
        if (10_000_000 < intersects):
            return -1

        active += starts[i] - ends[i]

    return intersects