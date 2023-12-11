# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N = len(A)
    if N == 0:
        return -1

    half = N // 2
        
    the_set = {}

    for i in A:
        if not the_set.get(i):
            the_set[i] = 1
        else:
            the_set[i] += 1

    the_set_sorted = dict(sorted(the_set.items(), key=lambda item: item[1], reverse=True))
    first_key = list(the_set_sorted.keys())[0]
    if the_set_sorted[first_key] <= half:
        return -1
    
    return A.index(first_key)