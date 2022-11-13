class Solution:
    def reverseWords(self, s: str) -> str:
        
        char_s = 0
        char_e = len(s)-1
        while char_s<len(s) and s[char_s] == ' ':
            char_s += 1
        while char_e>0 and s[char_e] == ' ':
            char_e -= 1
        
        s = s[char_s:char_e+1]
        
        words = []
        ss= 0
        i=0
        while i <(len(s)):
            if i==0 or s[i-1]==' ':
                ss=i
                i+=1
            elif s[i]== ' ':
                words.append(s[ss:i])
                
                while s[i]== ' ':
                    i+=1
                ss=i
            else: i+=1
         
        words.append(s[ss:i])

        res = ''
        for w in words[::-1]:
            res +=w+' '
            
        return res[:-1]