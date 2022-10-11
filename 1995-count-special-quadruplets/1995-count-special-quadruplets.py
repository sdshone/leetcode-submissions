class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        
        sumdiff = defaultdict(lambda: 0)
        count = 0
        # sumdiff[nums[len(nums)-1] - nums[len(nums)-2]] = 1
        for i in range(len(nums)-1, -1, -1):
            
            
            for j in range(i-1,-1,-1):
                
                _sum = nums[i] + nums[j]
                if _sum in sumdiff:
                    count += sumdiff[_sum]
            
            for k in range(len(nums)-1,i,-1):
                diff = nums[k] - nums[i]
                
                sumdiff[diff]+=1
        
        return count