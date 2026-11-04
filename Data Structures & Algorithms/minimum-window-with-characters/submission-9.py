from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        ds = defaultdict(int)
        for c in t:
            ds[c] += 1
        ref = len(ds)
        dt = defaultdict(int)
        cnt = 0
        idx = 0
        l = 0
        for end, c in enumerate(s):
            dt[c] += 1
            if dt[c] == ds[c]:
                cnt += 1
            while start <= end and dt[s[start]] > ds[s[start]]:
                dt[s[start]] -= 1
                start += 1
            if cnt == ref:
                if l == 0 or l > end - start + 1:
                    idx = start
                    l = end - start + 1
                dt[s[start]] -= 1
                start += 1
                cnt -= 1
        return s[idx:idx+l]