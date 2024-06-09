def solution(sizes):
    max_w = 0
    max_h = 0
    
    for w, h in sizes:
        wi = max(w, h)
        he = min(w, h)
        if wi > max_w:
            max_w = wi
        if he > max_h:
            max_h = he
    return max_w * max_h