import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [v for v in stones]
        heapq.heapify_max(h)
        while len(h) > 1:
            x = heapq.heappop_max(h)
            y = heapq.heappop_max(h)
            if x != y:
                heapq.heappush_max(h, abs(x - y)) 
        return h[0] if len(h) == 1 else 0