def solution(A): 
    A.sort() # O(n log n)

    #  Another math problem:
    # [-1000 -999 998 999 1000]
    # -1000 * -999 * 1000 = 999_000_000
    #   998 *  999 * 1000 = 997_002_000
    # So we need to account for the lowest 2 numbers if it has negative numbers

    highestPositive = A[-1] * A[-2] * A[-3] 
    highestNegative = A[-1] * A[0] * A[1]

    return max(highestPositive, highestNegative)