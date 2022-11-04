class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        s = [char for char in s]
        mapping = {}
        for i in range(len(s)):
            if s[i] in vowels:
                mapping[i]=s[i]
        
        idxs = list(mapping.keys())
        rev_idx = idxs[::-1]
        for idx in range(len(rev_idx)):
            s[idxs[idx]] = mapping[rev_idx[idx]]

        s = ''.join(s)
        return s
            