class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        
        products.sort()
        i, j = 0, len(products)-1
        res = []
        newsearch = products
        for idx,char in enumerate(searchWord):
            i, j = 0, len(newsearch)-1
            # print(newsearch)
            # print(res, i, j)
            while i<=j and (idx >= len(newsearch[i]) or newsearch[i][idx] < char):
                i+=1
            
            while i<=j and idx < len(newsearch[j]) and newsearch[j][idx] > char:
                j-=1
            
            newsearch = newsearch[i:j+1]
            res.append(newsearch[:3])
            
        return res