class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = [[target - position[i], speed[i]] for i in range(len(speed))]
        
        cars.sort(key=lambda x: x[0], reverse=False)
        
        time = cars[0][0]/cars[0][1]
        fleet = 1
        for car in cars:
            t = car[0]/car[1]
            if time <t:
                fleet+=1
            time = max(time, t)

        return fleet