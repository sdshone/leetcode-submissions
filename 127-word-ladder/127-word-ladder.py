class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # Solve using BFS
        if endWord not in wordList: return 0
        res = 1
        wordList = set(wordList)

        wordList.add(beginWord)
        neighbors = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+'X'+word[j+1:]
                neighbors[pattern].append(word)
        
        
        # print(neighbors)
        queue = collections.deque([beginWord])
        
        visited = set([beginWord])
        while queue:
            curLayer = set()
            for _ in range(len(queue)):
                
                word = queue.popleft()
                if word == endWord:
                    return res

                for i in range(len(word)):
                    pattern = word[:i]+'X'+word[i+1:]
                    # print(pattern)
                    for nextWord in neighbors[pattern]:

                        if nextWord not in visited:
                            queue.append(nextWord)
                            visited.add(nextWord)
            res+=1
            # visited.update(curLayer)
        
        return 0
