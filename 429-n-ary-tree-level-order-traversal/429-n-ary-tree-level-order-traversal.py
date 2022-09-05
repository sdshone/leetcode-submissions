"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root: return []
        q = deque()
        res = []
        
        q.append(root)
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.children:
                    for child in node.children:
                        q.append(child)
                
                level.append(node.val)
            res.append(level)
        return res