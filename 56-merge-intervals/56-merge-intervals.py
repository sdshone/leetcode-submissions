class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1: return intervals
        intervals.sort()
        
        new_intervals = [intervals[0]]
        
        for i in range(1,len(intervals)):
            l_new = len(new_intervals)
            if intervals[i][0] <= new_intervals[l_new-1][1]:
                new_intervals[-1][1] = max(new_intervals[-1][1], intervals[i][1])
                 
            else:
                 new_intervals.append(intervals[i])
        print(new_intervals)
        return new_intervals