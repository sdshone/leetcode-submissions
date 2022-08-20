class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        res = []
        visited = set()
        curr_path = set()
        def dfs(n, curr_path):
            
            if n in visited:
                return
            if n in curr_path:
                return -1
            for c in prereq[n]:
                curr_path.add(n)
                x=dfs(c, curr_path)
                if x==-1:
                    return x
            curr_path = set()
            visited.add(n)
            res.append(n)
            
        
        
        
        prereq = collections.defaultdict(set)
        for req in prerequisites:
            prereq[req[0]].add(req[1])
        
        for n in range(numCourses):  
            x=dfs(n, set())
            if x==-1:
                return []
        
        return res if len(res)==numCourses else []
            
            