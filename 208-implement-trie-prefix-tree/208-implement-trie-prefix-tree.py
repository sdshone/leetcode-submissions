class Node:
    def __init__(self,):
        self.children = {}
        self.endOfWord = False
class Trie:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        root = self.root
        for c in word:
            if c not in root.children:
                root.children[c] = Node()
            root = root.children[c]
        root.endOfWord = True
        
        
        
    def search(self, word: str) -> bool:
        if not word: return True
        root = self.root
        for c in word:
            if c not in root.children:
                return False
            root = root.children[c]
        return root.endOfWord
      

    def startsWith(self, prefix: str) -> bool:
        if not prefix: return True
        root = self.root
        for c in prefix:
            if c not in root.children:
                return False
            root = root.children[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)