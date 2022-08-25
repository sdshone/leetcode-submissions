class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magzineCounter = collections.Counter(magazine)
        ransomCounter = collections.Counter(ransomNote)
        
        for char in set(ransomNote):
            if ransomCounter[char]>magzineCounter[char]:
                return False
        return True