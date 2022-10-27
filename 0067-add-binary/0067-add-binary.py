class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        
        carry = 0
        A = len(a)
        B = len(b)
        
        if A < B:
            a = '0'*(B-A) + a
            A = B
        elif B < A:
            b = '0'*(A-B) + b
            B = A
        ans=''
        for i in range(B-1,-1,-1):
            
            total = int(b[i]) + int(a[i]) + carry
            if total == 3:
                carry = 1
                tans = '1'
            elif total == 2:
                carry = 1
                tans = '0'
            else:
                carry = 0
                tans = str(total)
            ans+=tans
        if carry:
            ans+='1'
        
        return ans[::-1]