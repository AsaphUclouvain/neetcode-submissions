class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0,0,0]
        for i in range(len(triplets)):
            x, y, z = target
            a, b, c = triplets[i]
            if a == x or b == y or c == z:
                if not (a > x or b > y or c > z):
                    res[0] = max(res[0], a)
                    res[1] = max(res[1], b)
                    res[2] = max(res[2], c)
        return res == target