class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        merged = []
        intervals.sort(key=lambda i: -i[1])
        last = list(intervals[0])
        for a, b in intervals:
            if b >= last[0]:
                last[0] = min(a, last[0])
            else:
                merged.append(last)
                last = [a, b]
        merged.append(last)
        return merged
