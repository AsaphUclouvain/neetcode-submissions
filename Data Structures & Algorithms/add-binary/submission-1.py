class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        a, b = a[::-1], b[::-1]
        c = 0
        for i in range(max(len(a), len(b))):
            digA = ord(a[i]) - ord('0') if i < len(a) else 0
            digB = ord(b[i]) - ord('0') if i < len(b) else 0

            tot = digA + digB + c
            res.append(str(tot % 2))
            c = tot // 2
        if c == 1:
            res.append('1')
        return ''.join(res[::-1])

