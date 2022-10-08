class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        N = len(nums)
        closest=sum(nums[:3])
        nums.sort()
        for i in range(N-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j, k = i+1, N-1

            while j<k:
                
                sum_3 = nums[i]+nums[j]+nums[k]
                # print(i,j,k)
                if target==sum_3: return target
                elif(abs(closest-target)> abs(sum_3-target)):
                    closest=sum_3
                if sum_3 > target:
                    k-=1
                else:
                    j+=1
                
                
                
                
        return closest