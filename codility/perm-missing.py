def solution(A):
    total_sum = 0
    for i in range(0, len(A)+1):
        total_sum += i+1

    return total_sum - sum(A)