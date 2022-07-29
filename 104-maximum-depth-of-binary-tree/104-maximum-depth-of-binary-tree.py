# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        max_depth = 0
        def findDepth(node, depth):
            nonlocal max_depth
            if not node: return 
            print(depth)
            max_depth = max(depth, max_depth)
            findDepth(node.left, depth+1)
            findDepth(node.right, depth+1)
            
            
            
        findDepth(root, 1)
        return max_depth