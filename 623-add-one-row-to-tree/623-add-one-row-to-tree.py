# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            return TreeNode(val, root, None)
        
        q = collections.deque()
        
        q.append(root)
        level = 0
        while q:
            level += 1
            for i in range(len(q)):
                # print(q)
                node = q.popleft()
                # if level >= depth:
                #     break
                if level == depth-1:
                    node.left = TreeNode(val,node.left, None)
                    node.right = TreeNode(val,None, node.right)
                    # break
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                # print(root)
                
            if level == depth-1:
                break
        return root
                    