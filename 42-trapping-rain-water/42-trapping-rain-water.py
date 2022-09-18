class Solution:
    def trap(self, height: List[int]) -> int:

        
        maxL, maxR = height[0], height[-1]
        
        left, right = 0, len(height) - 1
        
        res = 0
        while left <= right:
            
            # print(left, right, res, maxL, maxR)
            if height[left] < height[right]:
                
                
                res += maxL-height[left] if maxL-height[left]>0 else 0
                maxL = max(maxL, height[left])
                left +=1
            
            else:
                
                res += maxR-height[right] if maxR -height[right]>0 else 0
                maxR = max(maxR, height[right])
                right -=1
                
            
        
            
        return res