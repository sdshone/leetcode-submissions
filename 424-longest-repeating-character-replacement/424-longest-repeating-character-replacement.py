class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        i, j = 0, 0
        count = collections.Counter(s[0])
        maxf = 0
        longest = 0
        while j < len(s) and i<=j:
            maxf = max(maxf,count[s[j]])
            if (j-i+1) - maxf <=k:
                longest = max(longest, j-i+1)
                j+=1
                if j < len(s):
                    count[s[j]]+=1
            else:
                count[s[i]]-=1
                i+=1
                
            print(i,j,longest,maxf)
        return longest