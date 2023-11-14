def solution(A):
    # Organize 
    A.sort() # O(n)
    min_value = 1
    last_check = None
    for i in A: # O(n) worst case scenario
        if i <= 0:
            continue

        if last_check == i:
            continue
        
        if i == min_value:
            min_value += 1
            last_check = i
        else:
            return min_value
    
    return min_value