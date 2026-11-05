class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        v = n
        while v != 1:
            if v in s:
                return False
            s.add(v)
            a = 0
            for c in str(v):
                a += (int(c))**2
            v = a
        return True
