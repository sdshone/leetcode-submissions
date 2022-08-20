class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        
        # target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
        
        dp = [startFuel] + [0]*len(stations)
        for i, (loc, cap) in enumerate(stations):
            for j in range(i,-1,-1):
                if dp[j] >= loc: # the fuel tank is reachable
                    dp[j+1] = max(dp[j+1], dp[j]+ cap) # updating max count for next station

                
        for i,d in enumerate(dp):
            if d >= target: return i
        return -1