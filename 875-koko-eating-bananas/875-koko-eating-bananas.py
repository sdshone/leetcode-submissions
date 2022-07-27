class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_speed = right
        while left <= right:
            mid = (left + right) // 2

            time = sum([math.ceil(p/mid) for p in piles])
            if time <= h:
                min_speed = min(mid, min_speed)
                right = mid - 1
            else:
                left = mid + 1
        return min_speed
                