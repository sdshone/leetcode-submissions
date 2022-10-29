# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(node, h):

            if not node.left and not node.right: 

                return h+1
        
            x = y = float('inf')
            if node.left:
                x = dfs(node.left, h+1)
            if node.right:
                y = dfs(node.right, h+1)

            return min(x, y)
        
        if not root: return 0
        return dfs(root, 0)