class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        charset = set()
        for char in sentence:
            charset.add(char)
        
        return len(charset)==26