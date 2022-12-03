class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = defaultdict(int)
        
        for char in s:
            count[char]+=1
        new_s = ''
        for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True):
            new_s += k*v
        return new_s