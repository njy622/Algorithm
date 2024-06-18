class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dict = {indices[i]: s[i] for i in range(len(indices))}
        res = ''.join([dict[i] for i in range(len(indices))])
        return res
        