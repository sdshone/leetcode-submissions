# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        
        count = 0
        def dfs(node, level):
            nonlocal count
            if not node:
                count +=1
                return
            dfs(node.right, level+1)
            # print(level)
            dfs(node.left, level+1)
            # print(c2)
            return 
        dfs(root, 0)
        return (count-1)