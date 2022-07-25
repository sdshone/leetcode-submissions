class Solution:
    def maxArea(self, height: List[int]) -> int:
        #BRUTE FORCE APPROACH
        
        # max_area = float('-inf')
        # for i in range(len(height)):
        #     for j in range(len(height)):
        #         area = abs(i-j) * min(height[i], height[j])
        #         max_area = max(max_area, area)
        # return max_area
        
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(area, max_area)
            
            if height[left] > height[right]:
                right -=1
            else:
                left +=1
        return max_area
            