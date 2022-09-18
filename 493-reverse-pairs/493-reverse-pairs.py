class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        def helper(nums, low, mid, high):
            
            count = 0
            j = mid+1
            
            for i in range(low, mid+1):
                
                while j <= high and nums[i] > 2*nums[j]:
                    j+=1
                count +=( j - (mid+1))

            temp =[]
            left=low
            right=mid+1
            
            while left <=mid and right <=high:
                if nums[left]< nums[right]:
                    temp.append(nums[left])
                    left+=1
                else:
                    temp.append(nums[right])
                    right+=1
            while left<= mid:
                temp.append(nums[left])
                left+=1
        
            while right<= high:
                temp.append(nums[right])
                right+=1
                
            # print(high, low, temp)
            for i in range(low, high+1):
                nums[i] = temp[i-low]
            
            return count
        
        def merge(nums, low, high):
            
            if low >= high:
                return 0
            mid = (low+high)//2
            count = merge(nums, low, mid)             
            count += merge(nums, mid+1, high)
            count += helper(nums, low, mid, high)
            # print(nums)
            return count
        
        return merge(nums, 0, len(nums)-1)
        