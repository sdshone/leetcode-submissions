"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node1: 'Node') -> 'Node':
        visited = defaultdict(set)
        if not node1: return
        def dfs(node):
            
            new_node = Node(node.val)
            for n in node.neighbors:
                
                if n.val not in visited[node.val]:
                    visited[node.val].add(n.val)
                    x=dfs(n)
                    new_node.neighbors.append(x)
            return new_node
        x=dfs(node1)

        nodes = {n:Node(n) for n in visited.keys()}
        if not nodes:
            return x
        return_node = None
        for k,v in visited.items():
            for value in v:
                nodes[k].neighbors.append(nodes[value])
            if k == node1.val:
                return_node = nodes[k]
        return return_node