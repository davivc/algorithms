# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# <-4     <-2 <-1 <-5
#     3->

# <-4     <-1 <-5
#     3->

# <-4     <-5
#     3->

# <-4 <-5
#
#####
# 4->     2-> 1-> 5->
#     <-3

def solution(A, B):
    n = len(A)
    river = []

    for i in range(len(A)):
        size = A[i]
        direction = B[i]
        if direction == 0:
            while river and river[-1] < size:
                river.pop()
                n -= 1

            n -= 1 if river else 0
        else:
            river.append(size)
        
    return n