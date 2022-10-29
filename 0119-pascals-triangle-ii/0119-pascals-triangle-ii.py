class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0: return [1]
        nums = [1,1]
        
        for i in range(1,rowIndex):
            temp_nums = [1]
            for j in range(1,len(nums)):
                temp_nums.append(nums[j-1]+nums[j])
            temp_nums.append(1)
            nums = temp_nums
        return nums