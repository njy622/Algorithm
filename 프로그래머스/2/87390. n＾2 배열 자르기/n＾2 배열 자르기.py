def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        a = i//n # 몫
        b = i%n #나머지 값
        if a<b: a,b =b,a # 조금 더 큰 값 구하기
        answer.append(a+1)
    
    return answer