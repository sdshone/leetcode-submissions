# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root: return False
        def dfs(node, path):
            
            if not node.left and not node.right:
                return sum(path +[node.val]) == targetSum
            x, y = False, False
            if node.left:
                x = dfs(node.left, path + [node.val])
            if node.right:
                y = dfs(node.right, path + [node.val])
            return  x or y
        
        return dfs(root, [])