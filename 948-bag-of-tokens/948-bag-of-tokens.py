class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        
        i, j = 0, len(tokens) - 1
        
        if j == 0: return int(power > tokens[i])
        res = 0
        rres = 0
        while i<=j:
            # print(i,j)
            # print(tokens[i], power)
            # print(res)
            if tokens[i]<= power:
                power -= tokens[i]
                i += 1
                res += 1
            elif res > 0:
                power += tokens[j]
                j -= 1
                res -= 1
            else: break
            rres = max(res,rres)
        return rres