class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        d = defaultdict(list)
        for n in arr:
            d[(abs(n-x))].append(n)
        res = []
        count = 0
        for key in sorted(d.keys()):
            
            res.extend(d[key])
            count += len(d[key])
            if count >= k:
                break
        return sorted(res[:k])