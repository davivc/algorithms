def solution(S, P, Q):
    K = min(len(P), len(Q))

    S_arr = [*S]

    sum_arr_a = [0]
    sum_arr_c = [0]
    sum_arr_g = [0]    

    for i in range(0, len(S_arr)):
        a = sum_arr_a[i]
        c = sum_arr_c[i]
        g = sum_arr_g[i]
        if S_arr[i] == "A":
            a += 1
        elif S_arr[i] == "C":
            c += 1
        elif S_arr[i] == "G":
            g += 1
        
        sum_arr_a.append(a)
        sum_arr_c.append(c)
        sum_arr_g.append(g)
     
    answer = []
    for j in range(K):
        start = P[j]
        end = Q[j]+1

        if end > len(sum_arr_a) or start > len(sum_arr_a):
            continue 

        minimal = 4
        if sum_arr_a[end]-sum_arr_a[start] > 0:
            minimal = 1
        elif sum_arr_c[end]-sum_arr_c[start] > 0:
            minimal = 2
        elif sum_arr_g[end]-sum_arr_g[start] > 0:
            minimal = 3

        answer.append(minimal)

    return answer