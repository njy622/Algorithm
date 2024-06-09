def solution(nums):
    # 가져가도 되는 포켓몬 수
    pickPkm = len(nums)//2
    # 포캣몬 종류
    typePkm = len(set(nums))
    
    return min(typePkm, pickPkm)
