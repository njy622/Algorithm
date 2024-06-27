class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dicts = {}
        for i in range(len(mat)):
            dicts[i] = mat[i].count(1)
        sorted_dicts = sorted(dicts.items(), key=lambda item: item[1])
        list = []
        for key, val in sorted_dicts:
            list.append(key)
        return list[:k]