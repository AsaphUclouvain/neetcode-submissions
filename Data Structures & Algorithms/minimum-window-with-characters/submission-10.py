from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dt = defaultdict(int)
        for c in t:
            dt[c] += 1
        t_cnt = len(dt)
        ds = defaultdict(int)
        s_cnt = 0
        start = 0
        start_res = 0
        l = 0
        for end, c in enumerate(s):
            ds[c] += 1
            if ds[c] == dt[c]:
                s_cnt += 1
            while start <= end and ds[s[start]] > dt[s[start]]:
                ds[s[start]] -= 1
                start += 1
            if s_cnt == t_cnt:
                if l == 0 or l > end - start + 1:
                    l = end - start + 1
                    start_res = start
                ds[s[start]] -= 1
                start += 1
                s_cnt -= 1
        return s[start_res:start_res+l]
                
        