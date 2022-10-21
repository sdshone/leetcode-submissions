class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        
        d = defaultdict(list)
        for i,n in enumerate(nums):

            for num in d[n]:
                if abs(num-i)<=k:
                    return True
            d[n].append(i)
        return False
