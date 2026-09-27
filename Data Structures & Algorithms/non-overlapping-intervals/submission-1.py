class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        count = 0
        intervals.sort()
        last = intervals[0]
        for i in range(1, n):
            if last[1] > intervals[i][0]:
                count += 1
                if last[1] > intervals[i][1]:
                    last = intervals[i]
            else:
                last = intervals[i]              
        return count

        