class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        palindromic_substring = ''
        
        for idx in range(len(s)):
            
            left, right = idx, idx
            while left >= 0 and right < len(s) and s[left] == s[right]:
                
                if (right - left + 1) > len(palindromic_substring):
                    palindromic_substring = s[left: right+1]
                left -= 1
                right += 1
                    
            left, right = idx, idx + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                
                if (right - left + 1) > len(palindromic_substring):
                    palindromic_substring = s[left: right+1]
                left -= 1
                right += 1
                    
            print(palindromic_substring)
        return palindromic_substring