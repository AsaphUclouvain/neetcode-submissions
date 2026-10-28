class Solution:
    def myPow(self, x: float, n: int) -> float:
        def Hpow(x: float, n: int):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n == -1:
                return 1/x
            if n % 2 == 0:
                return Hpow(x*x, n//2)
            return x * Hpow(x, n - 1)

        if n > 0:
            return Hpow(x, n)
        return 1/Hpow(x, abs(n))