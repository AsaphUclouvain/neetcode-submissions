class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = ["" for i in range(len(num1) * len(num2) + 1)]
        idx = len(res) - 1
        
        for v1 in num1[::-1]:
            c = 0
            l = 0
            for v2 in num2[::-1]:
                c, r = divmod((int(v2) * int(v1) + c + int(res[idx] or '0')), 10)
                res[idx] = str(r)
                idx -= 1
                l += 1
            if c > 0:
                res[idx] = str(c)
                idx -= 1
                l += 1
            # print(res)
            idx += l - 1
            
        return "".join(res)
        