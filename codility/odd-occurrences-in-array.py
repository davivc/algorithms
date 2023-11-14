# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    val = 0
    for i in A:
        val ^= i

    return val