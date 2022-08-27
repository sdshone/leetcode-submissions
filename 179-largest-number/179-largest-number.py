class LargerKey(str):
    def __lt__(x,y):
        return x+y < y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums = [str(n) for n in nums]
        nums = sorted(nums, reverse=True, key = LargerKey)
        return ''.join(nums) if nums[0] != '0' else '0'