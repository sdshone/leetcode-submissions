class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        N = len(nums)
        ans = 0
        count = [defaultdict(int) for _ in range(N)]
        
        for i in range(N):
            for j in range(i):
                delta = nums[i] - nums [j]
                t = count[j][delta]
                count[i][delta] += t + 1
                ans += t
        # print(count)
        return ans