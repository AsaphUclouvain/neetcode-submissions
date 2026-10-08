import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries_idx = sorted([(q, i) for i, q in enumerate(queries)])
        hq = []
        i = 0
        res = [-1 for i in range(len(queries))]
        for q, idx in queries_idx:
            while hq and not (hq[0][1][0] <= q <= hq[0][1][1]):
                heapq.heappop(hq)
            while i < len(intervals):
                a, b = intervals[i]
                if a <= q <= b:
                    heapq.heappush(hq, (b - a + 1, (a, b)))
                elif a > q:
                    break
                i += 1
            if hq:
                res[idx] = hq[0][0]
        return res

            

# class Solution:
#     def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
#         res = [-1 for _ in range(len(queries))]
#         for i in range(len(queries)):
#             for a, b in intervals:
#                 if a <= queries[i] <= b:
#                     if res[i] > 0:
#                         res[i] = min(res[i], b - a + 1)
#                     else:
#                         res[i] = b - a + 1
#         return res

