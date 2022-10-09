import heapq
class MedianFinder:

    def __init__(self):
        self.max = []
        self.min = []

    def addNum(self, num: int) -> None:
        
        if len(self.max) == len(self.min):
            heapq.heappush(self.min, -heapq.heappushpop(self.max, -num))
        else:
            heapq.heappush(self.max, -heapq.heappushpop(self.min, num))
        

    def findMedian(self) -> float:
        # print(self.min, self.max)
        if len(self.max) == len(self.min):
            return (self.min[0]-self.max[0])/2
        else: 
            return self.min[0]
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()