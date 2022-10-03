class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        
        
        
        N, H = len(needle), len(haystack)
        i, j, nxt = 1, 0 , [-1]+[0]*N
        
        while i < N:
            if j == -1 or needle[i] == needle[j]:
                i, j = i+1, j+1
                nxt[i] = j
            else:
                j = nxt[j]
       
        i, j = 0, 0
        while i < H and j < N:
            
            if j == -1 or haystack[i] == needle[j]:
                i, j = i+1, j+1
                
            else:
                j = nxt[j]
        return i-j if j == N else -1
                    