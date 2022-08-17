class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        
        S_LEN = len(s)
        P_LEN = len(p)
        
        if S_LEN < P_LEN: return []
        
        
        s_counter = collections.Counter(s[:P_LEN])
        p_counter = collections.Counter(p)
        res = []
        if s_counter == p_counter:
            res.append(0)
        for i in range(1, S_LEN-P_LEN+1):
            
            s_counter[s[i-1]] -= 1
            s_counter[s[i+P_LEN-1]] +=1
            if s_counter == p_counter:
                res.append(i)
            

        return res