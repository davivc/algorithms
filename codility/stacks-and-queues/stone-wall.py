# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    walls = []
    blocks = 0

    for i in range(len(H)):
        while walls and H[i] < walls[-1]:
            walls.pop()
        
        if not walls or H[i] > walls[-1]:
            walls.append(H[i])
            blocks += 1

    return blocks