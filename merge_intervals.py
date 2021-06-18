class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        compare starts and ends
        see previous end greater than the next start
        create new interval with start equal to previous start and end equal to current end
        append that to intervals
        return intervals
        
        [1,5] [2,3]
        [[1,4],[0,2],[3,5]]
        """
        new_intervals = []
        intervals.sort()
        if len(intervals) < 2:
            return intervals
        for interval in intervals:
            if new_intervals == []:
                new_intervals.append(interval)
            elif new_intervals[-1][1] >= interval[0]:
                new_intervals[-1] = [min(new_intervals[-1][0],interval[0]), max(new_intervals[-1][1], interval[1])]
            else:
                new_intervals.append(interval)
        return new_intervals 