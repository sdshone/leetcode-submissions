class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        
        
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        for r,c in stones:
            rows[r].add((r,c))
            cols[c].add((r,c))
        visited = set()
        
        def dfs(r,c):
            visited.add((r,c))
            
            child = (rows[r].union(cols[c]) - visited)
            for r,c in child:
                dfs(r,c)
        
        islands = 0
        for r,c in stones:
            if (r, c) not in visited:
                dfs(r,c)
                islands +=1
        return len(stones) - islands