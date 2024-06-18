class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ''.join([{indices[i]: s[i] for i in range(len(indices))}[i] for i in range(len(indices))])
        return res
        