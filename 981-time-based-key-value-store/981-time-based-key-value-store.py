class TimeMap:

    def __init__(self):
        self.key_time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if not key in self.key_time_map:
            self.key_time_map[key] = {}
        self.key_time_map[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        
        if not key in self.key_time_map:
            return ""
        
        for t in range(timestamp, 0, -1):
            if t in self.key_time_map[key]:
                return self.key_time_map[key][t]
            
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)