# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = defaultdict(dict)
        
        def dfs(node, x, y):
            
            if not node:
                return
            
            if node.left:
                dfs(node.left, x+1, y-1)
            if node.right:
                dfs(node.right, x+1, y+1)
            
            if y not in res:
                res[y] ={}
            if x not in res[y]:
                res[y][x] = []
            res[y][x].append(node.val)
        
        
        dfs(root, 0, 0)
        final = []
        for keyy in sorted(res.keys()):
            f =[]
            for keyx in sorted(res[keyy].keys()):
                f.extend(sorted(res[keyy][keyx]))
            final.append(f)
        return final