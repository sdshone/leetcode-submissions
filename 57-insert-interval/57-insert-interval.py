class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        new_intervals = []
        
        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                new_intervals.append(intervals[i])
            elif newInterval[1] <intervals[i][0]:
                new_intervals.append(newInterval)
                return new_intervals + intervals[i:]
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
        new_intervals.append(newInterval)
        print(new_intervals)
        return new_intervals