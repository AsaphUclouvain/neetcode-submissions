class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        res = -1
        for i, c in enumerate(s):
            if c in d:
                res = max(res, i - d[c] - 1)
            else:
                d[c] = i
        return res