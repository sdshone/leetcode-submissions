class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        
        trials = (minutesToTest/ minutesToDie) + 1
        pigs  = 0
        while pow(trials, pigs) < buckets:
            pigs+=1
        return pigs