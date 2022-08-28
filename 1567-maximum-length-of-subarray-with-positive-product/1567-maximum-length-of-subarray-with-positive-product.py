class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        numsL = len(nums)
        start, end = 0, 0
        
        maxL = 0
        while start < numsL:
            while start < numsL and nums[start] == 0: start+=1
            end = start
            fneg, lneg, countneg = -1, -1, 0
            while end < numsL and nums[end] != 0:
                if nums[end] < 0:
                    countneg += 1
                    if fneg == -1: fneg = end
                    lneg = end
                end += 1
            if countneg % 2 == 0: currL = end - start
            else:
                currL = max(end - fneg -1, lneg - start)
                
            
            maxL = max(currL, maxL)

            start = end + 1
        return maxL