class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        d ={}
        for idx, word in enumerate(words):
            d[word] = idx
            
        res = set()
        
        for word in words: # "abcd", "cba"
            
            if word == "": continue
            elif word == word[::-1] and "" in d:
                res.add((d[word], d[""]))
                res.add((d[""], d[word]))
                
                
            rev = word[::-1]
            # "dcba"
            # print(rev)
            for i in range(len(rev)-1, -1, -1):
                rhs = rev[i:]
                # print(rhs)
                if rhs in d and rhs != word and word + rhs == (word + rhs)[::-1]:
                    res.add((d[word], d[rhs]))
                
            for i in range(1, len(rev)+1):
                lhs = rev[:i]
                # print(lhs)
                if lhs in d and lhs != word and lhs + word == (lhs + word)[::-1] :
                    res.add((d[lhs], d[word]))
        
        return sorted(res)