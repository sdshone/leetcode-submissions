class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        d = defaultdict(int)
        
        for w in words:
            d[w] += 1
        arr=[]
        for w in d:
            arr.append([d[w], w])
        arr.sort()
        arr.sort(key=lambda w: w[0], reverse=True)
        
        res = []
        for i in range(k):
            res.append(arr[i][1])
        return res