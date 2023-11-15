def solution(A):
    passing_cars = 0
    increment = 0

    for i in A: # O(n)
        if i == 0:
            increment += 1
        else:
            passing_cars += increment

        if passing_cars > 1_000_000_000:
            return -1

    return passing_cars