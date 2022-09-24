# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root: return []
        res = []
        
        def dfs(node, path):
            
            if not node.left and not node.right:
                path += [node.val]
                if sum(path) == targetSum:
                    res.append(path)
                return
            if node.left:
                dfs(node.left, path + [node.val])
            if node.right:
                dfs(node.right, path+ [node.val])
            
            
        dfs(root, [])
        return res