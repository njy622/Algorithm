class Solution:
    def isValid(self, s: str) -> bool:
        dict = {')':'(', '}':'{', ']':'['}
        isval = []

        for index in s:
            if index in dict:
                el = isval.pop() if len(isval) != 0 else ''
                if dict[index] != el:
                    return False
            else:
                isval.append(index)
        return len(isval) == 0