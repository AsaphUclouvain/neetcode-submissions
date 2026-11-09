class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            cnt = 0
            for t in range(32):
                if (i >> t) & 1 == 1:
                    cnt += 1
            res.append(cnt)
        return res
