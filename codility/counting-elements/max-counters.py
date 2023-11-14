# Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.

def solution(N, A): # O(n+m)
    counters = [0]*N # O(n)
    max_val = 0
    last_update = 0

    for K in A: # O(m)
        if K > N+1:
            continue
        
        if K == N+1:
            last_update = max_val
        else:
            counters[K-1] = max(counters[K-1], last_update) # O(2)
            counters[K-1] += 1 # O(1)
            max_val = max(counters[K-1], max_val) # O(2)

    for i in range(N): # O(n)
        if N[i] < last_update:
            N[i] = last_update

    return counters