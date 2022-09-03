class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        
        res = set()
        
        def dfs(num, count):
            
            if count == n:
                res.add(num)
                return
            
            last = num % 10
            nxt = last + k
            if 0 <= nxt < 10:
                
                new_num = num * 10 + nxt
                dfs(new_num, count+1)
            nxt = last - k
            if 0 <= nxt < 10:
                
                new_num = num * 10 + nxt
                dfs(new_num, count+1)
        
        for i in range(1, 10):
            dfs(i, 1)
        
        return sorted(list(res))
            
            