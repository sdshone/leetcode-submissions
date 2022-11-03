class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        
        worddict = defaultdict(int)
        
        for w in words:
            worddict[w]+=1
            
        ans = 0
        central = False
        for k, count in worddict.items():
            if k[0] == k[1]:
                if count % 2 == 0:
                    ans += count
                else:
                    ans += count - 1
                    central = True
            elif k[0]<k[1] and k[::-1] in worddict:
                ans += 2* min(count, worddict[k[::-1]])
        if central: ans+=1
        return 2*ans