# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        if not root: return []
        
        q = collections.deque()
        
        q.append(root)
        reverse = False
        res = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            
            if reverse:
                level.reverse()
            res.append(level)
            reverse = not reverse
        print(res)
        return res