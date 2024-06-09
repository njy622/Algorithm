def solution(answers):
    s1s = [1, 2, 3, 4, 5]
    s2s = [2, 1, 2, 3, 2, 4, 2, 5]
    s3s = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    mul = (len(answers) // len(s1s)) + 1
    s1s = s1s * mul
    s2s = s2s * mul
    s3s = s3s * mul

    point_dict = {1: 0, 2: 0, 3: 0}

    point_dict[1] += sum(1 for i in range(len(answers)) if s1s[i] == answers[i])
    point_dict[2] += sum(1 for i in range(len(answers)) if s2s[i] == answers[i])
    point_dict[3] += sum(1 for i in range(len(answers)) if s3s[i] == answers[i])

    max_ss = max(point_dict.values())

    point_list = [k for k, v in point_dict.items() if v == max_ss]

    return point_list