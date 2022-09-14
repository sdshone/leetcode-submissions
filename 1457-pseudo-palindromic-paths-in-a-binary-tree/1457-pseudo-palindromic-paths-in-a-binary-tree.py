# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        d =defaultdict(lambda: 0)
        res = 0
        def dfs(node):
            nonlocal res
            if not node: return
            
            d[node.val] += 1
            if not node.left and not node.right:
                
                odd_count = 0
                for key in d.keys():
                    if d[key] % 2 != 0: odd_count += 1
                    if odd_count > 1: break
                if odd_count <= 1: res += 1
            
            dfs(node.left)
            dfs(node.right)
            
            d[node.val] -= 1
            
        dfs(root)
        return res
            