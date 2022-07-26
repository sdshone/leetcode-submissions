class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0
        for num in nums:
            if num - 1 not in nums_set:
                count = 0
                while num+count in nums_set:
                    count += 1
                max_count = max(max_count, count)
        return max_count