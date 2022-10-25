class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        s1, s2 = '', ''
        
        M, N = len(word1), len(word2)
        m, n = 0, 0
        while m < M or n < N:
            if m< M:
                s1+=word1[m]
                m+=1
            if n< N:
                s2+=word2[n]
                n+=1
            if len(s1)== len(s2):
                if s1!=s2:
                    return False
            # print (s1, s2)
        return s1==s2
            