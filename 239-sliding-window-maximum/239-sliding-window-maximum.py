class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        
        q = collections.deque()
        q.append(nums[0])
        for i in range(1,k):
            
            while q and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
            
        # print(q)
        res = [q[0]]
        for i in range(k, len(nums)):
            if nums[i-k] == q[0]:
                q.popleft()
            while q and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
            res.append(q[0])
        # print(res)
        return res