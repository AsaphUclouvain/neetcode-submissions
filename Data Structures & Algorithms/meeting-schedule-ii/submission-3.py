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
        for i in intervals:
            line[i.start] += 1
            line[i.end] -= 1
        delta = 0
        ans = 0
        for k in sorted(line):
            delta += line[k]
            ans = max(ans, delta)
        return ans