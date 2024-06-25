class Solution:
    def calPoints(self, operations: List[str]) -> int:
        list_s = []
        length = len(operations)
        for i in operations:
            if i == "C":
                if list_s:
                    list_s.pop(-1)
            elif i == "D":
                if list_s:
                    m = list_s[-1] * 2
                    list_s.append(m)
            elif i == "+":
                if len(list_s) >= 2:
                    c = list_s[-2] + list_s[-1]
                    list_s.append(c)
            else:
                list_s.append(int(i))

        return sum(list_s)
