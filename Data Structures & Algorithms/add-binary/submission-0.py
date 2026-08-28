class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            short = a
            long = b
        else:
            short = b
            long = a
        i = 0
        a = long[::-1]
        b = short[::-1]
        res = []
        c = '0'
        while i < len(short):
            if a[i] == b[i] == '0':
                res.append(c)
                c = '0'
            if a[i] == b[i] == '1':
                if c == '1':
                    res.append('1')
                else:
                    res.append('0')
                    c = '1'
            if a[i] != b[i]:
                if c == '1':
                    res.append('0')
                else:
                    res.append('1')
            i += 1
        while i < len(a):
            if a[i] == c == '0':
                res.append('0')
            elif a[i] == c == '1':
                res.append('0')
            else:
                res.append('1')
                c = '0'
            i += 1
        if c == '1':
            res.append(c)
        return ''.join(res[::-1])
                

