def solution(A):
    len_list = len(A) # O(1)
    if len_list == 0:
        return 0

    # Removing duplicates
    A_set = set(A) # O(n)
    len_set = len(A_set) # O(1)
    if len_list != len_set:
        return 0

    # max() is O(n) and A.sort(),A[-1] is O(nlogn)
    max_val = max(A) # O(n)
    if len_set != max_val:
        return 0

    return 1