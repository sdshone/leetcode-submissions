import random
class Solution:

    def __init__(self, w: List[int]):
        
        self.list = []
        # print(len(w))
        W = len(w)
        for idx in range(len(w)):
            # if w[idx]:
            
            if W > 100:
                w[idx] = w[idx]%100
            self.list.extend([idx]*(w[idx]))
            
        
        random.shuffle(self.list)
    def pickIndex(self) -> int:
        return random.choices(self.list, k=1)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()