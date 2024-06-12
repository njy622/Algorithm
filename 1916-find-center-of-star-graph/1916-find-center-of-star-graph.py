class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for i in range(1, len(edges)):
            for j in range(2):
                for k in range(2):
                    if edges[i-1][j] == edges[i][k]:
                        return edges[i-1][j]


