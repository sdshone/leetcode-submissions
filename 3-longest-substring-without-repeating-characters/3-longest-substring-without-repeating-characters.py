class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        

        left, right = 0, 0
        len_s = len(s)
        maxL = 0
        
        curr_chars = set()
        while right < len_s:
            
            while s[right] in curr_chars:
                curr_chars.remove(s[left])
                left+=1
            curr_chars.add(s[right])
            maxL = max(maxL, right - left + 1)
            right += 1
        
        return maxL