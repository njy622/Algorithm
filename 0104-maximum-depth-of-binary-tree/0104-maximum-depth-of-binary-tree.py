# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            # 초기 스택값 : 부모노드 , 깊이
            stack = [(root, 1)]
            max_depth = 0
            while stack:
                # 자식 노드, 깊이는 stack에 있는 값을 꺼내옴
                node, depth = stack.pop()
                # 가장 깊은 것은 max_depth와 depth를 비교했을때, 가장 큰것
                max_depth = max(max_depth, depth)
                # 왼쪽 자식 노드가 있으면
                if node.left:
                    # stack안에 자식의 노드값과 깊이 +1 
                    stack.append((node.left, depth+1))
                # 오른쪽 자식 노드가 있으면
                if node.right:
                     # stack안에 자식의 노드값과 깊이 +1 
                    stack.append((node.right, depth+1))
            return max_depth