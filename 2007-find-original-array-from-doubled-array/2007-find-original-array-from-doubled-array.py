class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        if len(changed)%2 != 0: return []
        
        count = defaultdict(lambda: 0)
        for i in range(len(changed)):
            count[changed[i]]+=1
            
        ans = []
        for key in sorted(count.keys()):
            # print(count)
            # print(key, count[key], count[key*2])
            
            if count[key] > count[key*2]: return []
            
            if key == 0:
                if count[key]%2 != 0: return []
                else: ans.extend([0]*(count[0]//2))
            else:
                ans.extend([key]*(count[key]))
            count[key*2] -= count[key]
            
        return ans
            
        
        
#         changed.sort()
#         seen = set()
#         res = []
#         for i in range(len(changed)):
            
#             if changed[i]/2 in seen and changed[i]%2==0:
#                 seen.pop(changed[i]/2)
#                 res.append(int(changed[i]/2))
#             else:
#                 seen.add(changed[i])

        
#         return [] if seen else res
            