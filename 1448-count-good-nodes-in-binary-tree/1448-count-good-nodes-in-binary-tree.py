# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init(self):
        self.goodNodes = 0
    def goodNodes(self, root: TreeNode) -> int:

        self.goodNodes = 0
        def dfs(root, parent_val):    
            
            if not root:
                return
            
            if root.val >= parent_val:
                print(root.val, parent_val)
                self.goodNodes +=1
            dfs(root.left, max(parent_val, root.val))
            dfs(root.right, max(parent_val, root.val))

        dfs(root, root.val-1)
        # print(self.goodNodes)
        return self.goodNodes