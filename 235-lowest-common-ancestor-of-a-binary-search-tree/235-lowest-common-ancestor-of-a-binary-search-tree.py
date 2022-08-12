# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        left = min(p.val, q.val)
        right = max(p.val, q.val)
        
        if root.val < left:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > right:
            return  self.lowestCommonAncestor(root.left, p, q)
        else:
            return root