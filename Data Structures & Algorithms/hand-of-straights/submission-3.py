import heapq
from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        dic = defaultdict(int)
        for v in hand:
            dic[v] += 1
        h = [k for k in dic]
        heapq.heapify(h)
        while h:
            pop = []
            for _ in range(groupSize):
                if len(h) == 0:
                    return False
                v = heapq.heappop(h)
                pop.append(v)
                dic[v] -= 1
            for i in range(groupSize - 1):
                if pop[i + 1] > pop[i] + 1:
                    return False
            for v in pop:
                if dic[v] > 0:
                    heapq.heappush(h, v)
        return True
