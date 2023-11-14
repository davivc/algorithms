# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    max_gap = 0
    N_bin = bin(N)
    N_bin = N_bin[2:]
    N_array = N_bin.split('1')
    N_array_len = len(N_array)

    if N_array_len < 3:
        return max_gap

    for i in range(1, N_array_len-1):
        max_gap = max(len(N_array[i]), max_gap)

    return max_gap

