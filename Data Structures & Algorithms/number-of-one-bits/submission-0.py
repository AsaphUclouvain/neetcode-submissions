class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n > 0:
            n, r = divmod(n, 2)
            cnt += int(r == 1)
        return cnt