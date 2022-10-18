class Solution:
    def countAndSay(self, n: int) -> str:
        s='1'
        def countsay(s):
            pass
        for i in range(n-1):
            res=''
            idx=0
            while idx<len(s):
                char=s[idx]
                count = 0
                while idx<len(s) and s[idx]==char:
                    idx+=1
                    count+=1
                res+=f'{count}{char}'
            s=res 
        
        return s