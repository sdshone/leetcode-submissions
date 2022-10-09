class MyStack:

    def __init__(self):
        
        self.queue = deque()
        self.temp = deque()

    def push(self, x: int) -> None:
        
        self.queue.append(x)

    def pop(self) -> int:
        
        while not self.empty():
            res = self.queue.popleft()
            if not self.empty():
                self.temp.append(res)
            
        
        while self.temp:
            self.queue.append(self.temp.popleft())
        return res

    def top(self) -> int:
        
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()