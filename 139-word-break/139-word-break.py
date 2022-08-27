class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        dp = [False] * (len(s)+1)
        dp[-1] = True
        for idx in range(len(s)-1, -1, -1):
            
            for word in wordDict:
                if word == s[idx:idx+len(word)]:
                    dp[idx] = dp[idx+len(word)]
                if dp[idx]:
                    break
        return dp[0]