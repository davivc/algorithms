# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    val = 0
    for i in A: # 0(n)
        val ^= i

    return val