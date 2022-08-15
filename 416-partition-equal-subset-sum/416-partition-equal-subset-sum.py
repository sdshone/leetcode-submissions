class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums)%2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums)//2
        for num in nums:
            temp = set()
            for sums in dp:
                temp.add(sums+num)
            dp.update(temp)
        return target in dp