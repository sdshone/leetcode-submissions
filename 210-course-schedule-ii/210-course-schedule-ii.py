class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        res = []
        visited = set()
        curr_path = set()
        def dfs(n):
            if n in curr_path:
                return False            
            if n in visited:
                return True

            curr_path.add(n)
            for c in prereq[n]:
                if not dfs(c):
                    return False
            curr_path.remove(n)
            visited.add(n)
            res.append(n)
            return True
        
        
        
        prereq = collections.defaultdict(set)
        for req in prerequisites:
            prereq[req[0]].add(req[1])
        
        for n in range(numCourses):  
            if not dfs(n):
                return []
        
        return res
            
            