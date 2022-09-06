# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def dfs(node):
            
            if not node:
                return False
            curr = node.val == 1
            left = dfs(node.left)
            right = dfs(node.right)
            if not left:
                node.left = None
            if not right:
                node.right = None
            
            return left or right or curr
        
        dfs(root)
        if root.val == 0 and not root.left and not root.right:
            return None
        
        return root