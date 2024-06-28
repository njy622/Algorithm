class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(sorted(s)[-2::-1])+'1'
