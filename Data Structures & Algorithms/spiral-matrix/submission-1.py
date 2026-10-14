class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res: list[int] = []
        def record_loop(i: int, j:int, m: int, n: int):
            for k in range(j, n):
                res.append(matrix[i][k])
            for k in range(i + 1, m):
                res.append(matrix[k][n - 1])
            if m - 1 > i:
                for k in range(n - 2, j - 1, -1):
                    res.append(matrix[m - 1][k])
            if n - 1 > j:
                for k in range(m - 2, i, -1):
                    res.append(matrix[k][j])
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0, 0
        for dx in range((min(m, n) + 1) // 2):
            record_loop(i + dx, j + dx, m, n)
            m -= 1
            n -= 1
        return res
            