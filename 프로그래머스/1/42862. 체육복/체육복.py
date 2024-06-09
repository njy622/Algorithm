def solution(n, lost, reserve):
    N_lost = sorted([l for l in lost if l not in reserve])
    N_reserve = sorted([r for r in reserve if r not in lost])

    for i in N_lost[:]:            
        if i - 1 in N_reserve:
            N_lost.remove(i)
            N_reserve.remove(i-1)
        elif i + 1 in N_reserve:
            N_lost.remove(i)
            N_reserve.remove(i+1)

    return n-len(N_lost)
