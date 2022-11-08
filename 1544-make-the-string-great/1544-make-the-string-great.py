import string
class Solution:
    def makeGood(self, s: str) -> str:
        
        
        changed = True
        
        while changed:
            new_s = ''
            i=0
            while i <= (len(s)):

                if i < len(s)-1 and s[i] in string.ascii_lowercase and s[i+1] in string.ascii_uppercase and s[i].upper() == s[i+1]:
                    i+=1  
                
                elif i < len(s)-1 and s[i] in string.ascii_uppercase and s[i+1] in string.ascii_lowercase and s[i].lower() == s[i+1]:
                    
                    i+=1
                elif i <= len(s)-1:
                    new_s += s[i]
                i+=1

            changed = new_s != s
            s = new_s
                
            
        return s
            
            
            