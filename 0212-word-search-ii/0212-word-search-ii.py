class TrieNode:
    def __init__(self):
        
        self.children = defaultdict()
        self.isWord = None

    def addWord(self, word):
        
        curr = self
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = word
        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        ROWS, COLS = set(range(len(board))), set(range(len(board[0])))
        R,C = len(board), len(board[0])
        root = TrieNode()
        words = set(words)
        for word in words:
            root.addWord(word)
            
        wlen = len(words)
        res, visited = set([None]), set()
        count = 0
        def dfs(r, c, node):
            nonlocal count, wlen
            # if (board[r][c] not in node.children 
            # or (r,c) in visited):
            #     return
            
            
            if node.isWord not in res:
                res.add(node.isWord)
                count+=1
            if not node.children or count==wlen:
                return
            
            if c+1 <C and (r,c+1) not in visited and board[r][c+1] in node.children:
                visited.add((r,c+1))
                dfs(r, c+1, node.children[board[r][c+1]])
                visited.remove((r,c+1))
            if r+1 <R and (r+1,c) not in visited and board[r+1][c] in node.children:
                visited.add((r+1,c))
                dfs(r+1, c, node.children[board[r+1][c]])
                visited.remove((r+1,c))
            if c-1 >=0 and (r,c-1) not in visited and board[r][c-1] in node.children:
                visited.add((r,c-1))
                dfs(r, c-1, node.children[board[r][c-1]])
                visited.remove((r,c-1))
            if r-1 >=0 and (r-1,c) not in visited and board[r-1][c] in node.children:
                visited.add((r-1,c))
                dfs(r-1, c, node.children[board[r-1][c]])
                visited.remove((r-1,c))
    
        for r in ROWS:
            for c in COLS:
                if board[r][c] in root.children:
                    visited.add((r,c))
                    dfs(r, c, root.children[board[r][c]])
                    visited.remove((r,c))
        res.remove(None)
        return list(res)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        