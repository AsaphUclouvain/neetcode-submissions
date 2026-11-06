import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        heapq.heapify(h)
        res = []
        for i in range(k - 1):
            heapq.heappush(h, (-nums[i], i))

        for i in range(k - 1, len(nums)):
            heapq.heappush(h, (-nums[i], i))
            while h:
                t = h[0]
                if i - k + 1 <= t[1] <= i:
                    res.append(-t[0])
                    break
                heapq.heappop(h)
        return res

            