class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        counter = collections.Counter(arr).most_common()
        min_chars_to_remove = len(arr)//2
        minCount = 0
        
        for item in counter:
            minCount +=1
            if item[1] >= min_chars_to_remove:     
                return minCount
        
            min_chars_to_remove -= item[1]
        
        