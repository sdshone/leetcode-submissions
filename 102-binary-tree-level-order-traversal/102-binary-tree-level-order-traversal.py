# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        level_list = [root]
        return_list = []
        while level_list:
            l = []
            for i in range(len(level_list)):
                node = level_list.pop(0)
                if node.left:
                    level_list.append(node.left)
                if node.right:
                    level_list.append(node.right)
                    
                l.append(node.val)

            return_list.append(l)
        return return_list