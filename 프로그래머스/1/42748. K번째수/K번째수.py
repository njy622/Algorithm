def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a, b, c = commands[i]
        # print(a,b,c)
        rs_array = array[(a-1):b]
        # print(rs_array)
        rs_array.sort()
        answer.append(rs_array[c-1])
    return answer