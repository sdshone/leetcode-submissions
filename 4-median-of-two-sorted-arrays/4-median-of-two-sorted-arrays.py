class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        l_nums1 = len(nums1)
        l_nums2 = len(nums2)
        new_nums = []
        
        first, second = 0, 0
        while first < len(nums1) and second < len(nums2):
            if nums1[first] <= nums2[second]:
                new_nums.append(nums1[first])
                first+=1
            else:
                new_nums.append(nums2[second])
                second+=1
    
        new_nums.extend(nums1[first:])
        new_nums.extend(nums2[second:])
        x= len(new_nums)//2

        if len(new_nums)%2 == 0:
            
            return (new_nums[x]+new_nums[x-1])/2
        else:
            return new_nums[x]