class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        
        P = len(palindrome)
        if P==1: return ''
        p=list(palindrome)
        palindrome=list(palindrome)
        for i in range(P):
            if p[i]!='a':
                p[i]='a'
                break
        if set(p)==set('a'):
            palindrome[-1]='b'
        else: palindrome=p
        return ''.join(palindrome)