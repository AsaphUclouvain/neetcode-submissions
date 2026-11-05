from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for c in s1:
            d1[c] += 1
        ref = len(d1)
        cnt = 0
        start = 0
        for end, c in enumerate(s2):
            d2[c] += 1
            if d2[c] == d1[c]:
                cnt += 1
            while start <= end and d2[c] > d1[c]:
                if d2[s2[start]] == d1[s2[start]]:
                    cnt -= 1
                d2[s2[start]] -= 1
                start += 1
            if cnt == ref:
                return True
        return False
