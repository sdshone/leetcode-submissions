class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key=lambda box: box[1], reverse = True)
        boxL = len(boxTypes)
        packSize = 0
        curr = 0
        tUnits = 0
        while curr < boxL:
            
            units = min(truckSize-packSize, boxTypes[curr][0])
            
            packSize += units
            tUnits += units * boxTypes[curr][1]
            curr += 1
        
        return tUnits