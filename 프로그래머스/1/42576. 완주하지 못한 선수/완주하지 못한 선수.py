def solution(participant, completion):
    par = {}
    
    for i in participant:
        if i in par:
            par[i] += 1
        else: 
            par[i] = 1
    for i in completion:
        par[i] -= 1
    
    for i in participant:
        if not par[i] == 0:
            return i
        
    return