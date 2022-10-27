class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        N = len(img1)
        a ,b = [], []
        d = defaultdict(int)
        for row in range(N):
            for col in range(N):
                if img1[row][col]:
                    a.append((row, col))
                if img2[row][col]:
                    b.append((row, col))
        
        for ra, ca in a:
            for rb, cb in b:
                d[rb-ra, cb-ca]+=1
            # print(d)
        
        return max(d.values() or [0])