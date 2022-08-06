class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        visited = {}
        for i in range(len(s)):
                
            if s[i] in visited:
                if visited[s[i]]!= t[i]:
                    return False
            else:
                if t[i] in visited.values():
                    return False
                visited[s[i]] = t[i]

        return True