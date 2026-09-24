class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        handled = False
        i = 0
        n = len(intervals)
        res = []
        sweep = []
        while not handled or i < n:
            if not handled and (i == n or intervals[i] > newInterval):
                cur = newInterval
                handled = True
            else:
                cur = intervals[i]
                i += 1
            if not sweep:
                sweep = list(cur)
            elif cur[0] - sweep[1] <= 0:
                sweep[1] = max(sweep[1], cur[1])
            else:
                res.append(sweep)
                sweep = list(cur)
        res.append(sweep)
        return res
            
