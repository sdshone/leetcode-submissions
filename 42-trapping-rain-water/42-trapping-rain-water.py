class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        total = 0
        
        while left < right:
            
            if left_max < right_max:
                left +=1
                left_max = max(left_max, height[left])
                total += left_max - height[left]
            else:
                right-=1
                right_max = max(right_max, height[right])
                total += right_max - height[right]
                
        return total
                