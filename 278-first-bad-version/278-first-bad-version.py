# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        i, j = 0 , n
        min_version = n+1
        while i <= j:
            
            mid = (i + j) // 2
            
            if isBadVersion(mid):
                j = mid - 1
                min_version = min(min_version, mid)
            else:
                i = mid + 1
        return min_version
                