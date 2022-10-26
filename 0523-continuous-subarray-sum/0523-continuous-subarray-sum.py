class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        
        hashmap = {0:0}
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            # print(s,k,nums[i], hashmap)
            if s%k not in hashmap:
                hashmap[s%k]=i+1
            elif hashmap[s%k] < i:
                return True
        return False