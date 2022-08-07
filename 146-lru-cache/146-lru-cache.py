# doubly linked list to store the rencecy
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}

        
    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        
        prev.next = nxt
        nxt.prev = prev
        
        
        
    def insert(self, node: Node) -> None:
        prev, nxt = self.right.prev, self.right
        node.prev = prev
        node.next = self.right
        prev.next = nxt.prev = node
        
        
    def get(self, key: int) -> int:
        
        if key in self.cache:
            # make key most recent
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val 
            
        return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache.keys()) > self.cap:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)













