class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        
        if ax1 > ax2:
            ax1, ax2 = ax2, ax1
        if ay1 > ay2:
            ay1, ay2 = ay2, ay1
        if bx1 > bx2:
            bx1, bx2 = bx2, bx1
        if by1 > by2:
            by1, by2 = by2, by1
        
        t = abs(ax1 - ax2) * abs(ay1-ay2) + abs(bx1 - bx2) * abs(by1 - by2)

        overlapx = set(range(ax1, ax2)).intersection(set(range(bx1, bx2)))
        overlapy = set(range(ay1, ay2)).intersection(set(range(by1, by2)))
        return t - (len(overlapx)* len(overlapy))