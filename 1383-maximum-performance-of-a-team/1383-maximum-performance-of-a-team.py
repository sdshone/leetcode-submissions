class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        cur_sum = 0
        h = []
        ans = float('-inf')
        for e, s in sorted(zip(efficiency, speed), reverse = True):  

            while len(h) > k-1:
                cur_sum -= heappop(h)
            heappush(h, s)
            cur_sum += s
            ans = max(ans, cur_sum * e)
        
        return ans % (10**9 + 7)