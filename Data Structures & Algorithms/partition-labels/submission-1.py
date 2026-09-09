from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def list_two():
            return [5001, 0]
        dic = defaultdict(list_two)
        for i, c in enumerate(s):
            dic[c][0] = min(dic[c][0], i)
            dic[c][1] = max(dic[c][1], i)
        start = 0
        res = []
        while start < len(s):
            end = dic[s[start]][1]
            seen = {start, end}
            repeat = False
            for i in range(start, end):
                if i in seen:
                    continue
                if end < dic[s[i]][1]:
                    dic[s[start]][1] = dic[s[i]][1]
                    repeat = True
                    break
                seen.add(i)
            if repeat:
                continue
            res.append(end - start + 1)
            start = end + 1
        return res