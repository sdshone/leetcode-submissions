class TrieNode:
    def __init__(self):
        
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        
        curr = self
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True
        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        ROWS, COLS = len(board), len(board[0])
        
        root = TrieNode()
        for word in words:
            root.addWord(word)
            
        W_LEN = len(words)
        res, visited = set(), set()
        
        def dfs(r, c, node, word):
            
            if (board[r][c] not in node.children 
            or (r,c) in visited) or W_LEN == len(res):
                return
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            if r-1 >=0:
                dfs(r-1, c, node, word)
            if c+1 < COLS:
                dfs(r, c+1, node, word)
            if r+1 < ROWS:
                dfs(r+1, c, node, word)
            if c-1 >=0:
                dfs(r, c-1, node, word)

            visited.remove((r,c))
    
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        
        return list(res)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        