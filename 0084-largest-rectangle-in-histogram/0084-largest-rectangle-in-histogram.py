class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        
        # MONOTONIC STACK
        
        heights.append(0) # handling boundary case
        stack = [-1] # also boundary case
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] -1
                ans = max(ans, h*w)
            stack.append(i)
        #heights.pop()
        return ans