class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        MOD = 10 ** 9 + 7
        stack = []
        sum_minimum = 0
        ARR = len(arr)
        
        for i in range(ARR+1):
            while stack and (i == ARR or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i
                count = (mid - left) * (right - mid)
                sum_minimum += count * arr[mid]
            stack.append(i)
        return sum_minimum % MOD