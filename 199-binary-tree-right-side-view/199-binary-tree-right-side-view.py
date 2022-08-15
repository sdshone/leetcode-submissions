# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        # level order
        q  = collections.deque()
        
        q.append(root)
        return_list = []
        while q:
            level_list = []
            for _ in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_list.append(node.val)
            if level_list:
                return_list.append(level_list[-1])
        print(return_list)
        return return_list