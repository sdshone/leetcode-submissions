from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereq = defaultdict(list)
        for c in prerequisites:
            prereq[c[0]].append(c[1])
            
        visited = set()
        
        def dfs(course):
            
            if course in visited:
                return False
            if prereq[course] ==[]:
                return True
            visited.add(course)
            for p in prereq[course]:
                if not dfs(p):
                    return False
            visited.remove(course)
            prereq[course] = []
            return True
        for c in range(numCourses):
            if not dfs(c): return False
        return True