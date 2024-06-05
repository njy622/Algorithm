class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left, right = 0,0
        result = 0
        for i in s:
            if i == 'R':
                right += 1
            if i == 'L':
                left += 1
            if left == right : 
                result += 1
        return result
