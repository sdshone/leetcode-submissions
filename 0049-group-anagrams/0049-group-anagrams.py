class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        res = defaultdict(list)
        
        for s in strs:
            counter = [0]*26
            
            for char in s:
                counter[ord(char)-ord('a')]+=1
            res[tuple(counter)].append(s)
        return res.values()