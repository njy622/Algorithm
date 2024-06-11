class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for gri in grid:
            for g in gri:
                if g < 0:
                    count = count + 1

        return count