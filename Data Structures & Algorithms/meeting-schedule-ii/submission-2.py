"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import defaultdict
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        line: defaultdict[int, int] = defaultdict(int)
        keys: list[int] = []
        for i in intervals:
            line[i.start] += 1
            line[i.end] -= 1
        count = 0
        ans = 0
        keys = sorted(list(line.keys()))
        for k in keys:
            count += line[k]
            ans = max(ans, count)
        return ans