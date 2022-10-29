class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        curr_plant_time = 0
        res = 0
        indices = sorted(range(len(plantTime)), key=lambda x: -growTime[x])
        
        for i in indices:
            
            curr_plant_time += plantTime[i]
            # print(curr_plant_time)
            res = max(res, curr_plant_time + growTime[i])
            
        return res