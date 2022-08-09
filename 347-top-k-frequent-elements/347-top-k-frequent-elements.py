class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)
        for n in nums:
            count[n]+=1

        
        counter = [ (k,v) for k,v in count.items()]
        counter.sort(key=lambda x: x[1], reverse=True)
        return [counter[x][0] for x in range(k)]
    
    
        # for i in range(k):
        #     max_c = max(count.values())
        #     print(max_c)
        #     for k,v in count.items():
        #         if v == max_c:
        #             final.append(k)
        #     if len(final)>=k:
        #         return final[:k]
        #     count.pop(k)