class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_nums = len(nums)
        prefix_sum = [nums[0]]
        
        for index in range(1, l_nums):
            prefix_sum.append(prefix_sum[index - 1] + nums[index])
            
        if prefix_sum[l_nums-1] == nums[0]: return 0
        # if prefix_sum[l_nums-1] == nums[l_nums-1]: return l_nums - 1
        for index in range(1, l_nums):
            if prefix_sum[index-1] == prefix_sum[l_nums - 1]- prefix_sum[index]:
                return index
        return -1