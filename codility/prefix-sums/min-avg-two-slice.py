# This solution assumes that we only need to check slices of 2 or 3 elements
# It is a math problem

def solution(A):
    idx = 0
    min_avg = 10001
    n = len(A)
    # iterate through the list
    for i in range(n - 1):
        # get the average of 2 neighbors
        avg = (A[i] + A[i + 1]) / 2

        # update the minimum average and the index
        (idx, min_avg) = (i, avg) if avg < min_avg else (idx, min_avg)

        # try the same for a 3-element slice, if we can
        if i < n - 2:
            avg = (A[i] + A[i + 1] + A[i + 2]) / 3
            (idx, min_avg) = (i, avg) if avg < min_avg else (idx, min_avg)

    # return the starting index of the minimum-average slice
    return idx