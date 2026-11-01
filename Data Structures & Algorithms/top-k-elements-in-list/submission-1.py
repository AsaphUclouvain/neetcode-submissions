from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        uniq = []
        for v in nums:
            if v not in d:
                uniq.append(v)
            d[v]+= 1
        uniq.sort(key=lambda x: d[x], reverse=True)
        return uniq[:k]