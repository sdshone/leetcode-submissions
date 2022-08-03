class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()
        # nums=set(nums)
        # for first in range(len(nums)):
        #     for second in range(first+1, len(nums)):
        #         two_sum=(nums[first]+nums[second])
        #         num = two_sum * -1 if two_sum!=0 else 0
        #         try:
        #             third = nums.index(num, second+1, len(nums))
        #             if first!=second and second!=third and third!=first:
        #                 sol = [nums[first],nums[second],nums[third]]
        #                 sol.sort()
        #                 for r in result:
        #                     if r[0]==sol[0] and r[1]==sol[1] and r[2]==sol[2]:
        #                         break
        #                 else:
        #                     result.append(sol)
        #         except:
        #             continue
        # return result
        
        for first, _ in enumerate(nums):
            
            if first > 0 and nums[first-1] == nums[first]:
                continue
            
            second = first+1
            third = len(nums)-1
            
            while second < third:
                sum_of_three = nums[first] + nums[second] + nums[third]
                
                if sum_of_three>0:
                    third-=1
                elif sum_of_three<0:
                    second+=1
                else:
                    result.append([nums[first], nums[second], nums[third]])
                    second +=1

                    while second < third and nums[second] == nums[second-1]:
                        second+=1
                    
        return result
                    
            
                        
        
                    