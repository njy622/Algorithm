def solution(date1, date2):
    i = 0
    j = 1
    k = 2
    res = 0
    if date1 and date2:
        if date1[i] == date2[i]:
            if date1[j] == date2[j]:
                if date1[k] == date2[k]:
                    res = 0
                    return res
                if date1[k] < date2[k]:
                    res = 1
                    return res
                else:
                    if date1[k] > date2[k]:
                        res = 0
                        return res
            if date1[j] < date2[j]:
                if date1[k] == date2[k]:
                    res = 1
                    return res
                if date1[k] < date2[k]:
                    res = 1
                    return res
                if date1[k] > date2[k]:
                    res = 1
                    return res
                res = 1
                return res
            if date1[j] > date2[j]:
                if date1[k] == date2[k]:
                    res = 0
                    return res
                if date1[k] < date2[k]:
                    res = 0
                    return res
                if date1[k] > date2[k]:
                    res = 0
                    return res
                res = 0
                return res
        if date1[i] < date2[i]:
            if date1[j] == date2[j]:
                if date1[k] == date2[k]:
                    res = 1
                    return res
                if date1[k] < date2[k]:
                    res = 1
                    return res
                else:
                    if date1[k] > date2[k]:
                        res = 1
                        return res
            if date1[j] < date2[j]:
                res = 1
                return res
            if date1[j] > date2[j]:
                res = 1
                return res
        else:
            res = 0
            return res
        if not date1 and not date2:
            res = 0
            return res