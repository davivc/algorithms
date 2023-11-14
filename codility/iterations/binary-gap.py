
def solution(N):
    max_gap = 0
    N_bin = bin(N)
    N_bin = N_bin[2:]
    N_array = N_bin.split('1') # O(n)
    N_array_len = len(N_array) # O(1)

    if N_array_len < 3:
        return max_gap

    for i in range(1, N_array_len-1): # O(n)
        max_gap = max(len(N_array[i]), max_gap) # O(2)

    return max_gap

