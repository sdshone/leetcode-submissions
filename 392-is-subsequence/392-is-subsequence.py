class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        if not s: return True
        idx = 0    
                
        for c in t:
            print(c,s[idx], idx)
            if c== s[idx]:
                idx+=1
            if idx == len(s):
                break
            
        if idx<(len(s)):
            return False
        return True
                