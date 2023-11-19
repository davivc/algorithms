def solution(A):
    intersects=0
    n = len(A)

    # Create all starts and ends
    points = []
    for i in range(n):
        points.append((i-A[i], "s"))
        points.append((A[i]+i, "e"))

    # Order by second attribute (reverse is true because we need the s first)
    points.sort(key=lambda x: x[1], reverse=True)
    # Order by first attribute
    points.sort(key=lambda x: x[0])

    total_open=0
    for i in points:
        if (i[1] == "s"):
            intersects += total_open
            total_open += 1
        elif(i[1] == "e"):
            total_open -= 1
        # print("intersects", intersects,"\t Total:",total_open)

        if(intersects > 10_000_000):
            return -1
    return intersects