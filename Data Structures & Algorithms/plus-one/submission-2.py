class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in range(len(digits) - 1, -1, -1):
            c, digits[i] = divmod(digits[i] + c, 10)
        if c == 0:
            return digits
        digits.append(0)
        digits[0] = c
        return digits
