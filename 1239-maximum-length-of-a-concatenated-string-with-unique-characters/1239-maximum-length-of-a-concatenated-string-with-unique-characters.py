class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        res = ['']
        maxLen = 0
        
        for word in arr:
            for r in res:
                newRes = r+word
                if len(newRes)!=len(set(newRes)):
                    continue
                res.append(newRes)
                maxLen = max(maxLen, len(newRes))
            # print(res)
        return maxLen
    