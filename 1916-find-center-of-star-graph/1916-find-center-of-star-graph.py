class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for i in range(1, len(edges)):
            if edges[i-1][0] == edges[i][0]:
                return edges[i-1][0]
            if edges[i-1][1] == edges[i][0]:
                return edges[i-1][1]
            if edges[i-1][0] == edges[i][1]:
                return edges[i-1][0]
            if edges[i-1][1] == edges[i][1]:
                return edges[i-1][1]

