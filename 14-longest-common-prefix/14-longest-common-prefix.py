class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ''
        if not strs: return prefix
        strs.sort(key=lambda x: len(x))
  
        idx = 0
        for i in range(len(strs[0])):
            char = strs[0][i]
            flag = True
            for word in strs:
                if word[idx] != char: 
                    flag = False
            if flag:
                
                prefix += word[idx]
                idx+=1
            else: return prefix
                
        return prefix