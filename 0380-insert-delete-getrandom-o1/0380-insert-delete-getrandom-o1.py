class RandomizedSet:

    def __init__(self):
        self.idx_map = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.idx_map: return False
        
        
        self.arr.append(val)
        self.idx_map[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        
        if val not in self.idx_map: return False
        idx = self.idx_map[val]
        
        self.arr[idx] = self.arr[-1]
        self.idx_map[self.arr[-1]] = idx
        self.idx_map.pop(val)
        self.arr.pop()
        return True
        

    def getRandom(self) -> int:
        
        return random.choice(self.arr)
    

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()