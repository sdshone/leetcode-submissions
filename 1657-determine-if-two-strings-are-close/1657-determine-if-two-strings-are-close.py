class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2): return False
        
        c1 = defaultdict(int)
        c2 = defaultdict(int)
        
        for char in word1:
            c1[char]+=1
        for char in word2:
            c2[char]+=1
        
        return sorted(list(c1.keys()))==sorted(list(c2.keys())) and sorted(list(c1.values())) == sorted(list(c2.values()))