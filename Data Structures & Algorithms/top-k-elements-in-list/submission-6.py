from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            count[num] += 1
        for num, cnt in count.items():
            freq[cnt].append(num)

        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                if len(res) == k:
                    return res
                res.append(num)
        return res