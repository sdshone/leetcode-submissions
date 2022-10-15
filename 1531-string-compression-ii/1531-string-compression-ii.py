class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        N = len(s)
        memo = {}
        def dp(start, k):
            
            if (start, k) in memo:
                return memo[(start, k)]
            
            if start==N or N-start<=k:
                return 0
            ans = float('inf')
            count = defaultdict(int)
            mostfreq = 0
            
            for i in range(start, N):
                
                char = s[i]
                count[char] +=1
                mostfreq = max(mostfreq, count[char])
                
                compressed_len = 1 + (len(str(mostfreq)) if mostfreq>1 else 0)
                
                if k >= i-start+1-mostfreq:
                    ans = min(ans, compressed_len+dp(i+1, k - (i-start+1-mostfreq)))
            
            memo[(start, k)] = ans
            return ans
        return dp(0, k)