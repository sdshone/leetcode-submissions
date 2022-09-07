# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        traversal = []
        def dfs(node):
            
            if not node:
                return
            
            
            traversal.append(str(node.val))
            if not node.left and node.right:
                traversal.append('(')
                traversal.append(')')
            if node.left:
                traversal.append('(')
                dfs(node.left)
                traversal.append(')')
            if node.right:
                traversal.append('(')
                dfs(node.right)
                traversal.append(')')
            
        dfs(root)
        traversal = ''.join(traversal)
        return traversal