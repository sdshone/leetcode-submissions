class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0]*len(temperatures)
        
        for idx,temp in enumerate(temperatures):
            
            while stack and stack[-1][1] < temp:
                t = stack.pop()
                answer[t[0]] = idx - t[0]
            stack.append([idx,temp])
       
        return answer