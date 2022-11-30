class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        
        count = defaultdict(int)
        for num in arr:
            count[num] += 1
        x = list(count.values())
        
        return len(x) == len(set(x))