class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        for v in collections.Counter(s).values():
            if v%2==1:
                res+=1
        print(res)
        return len(s)- res+1 if res else len(s)