class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        def rotate_edge(i: int):
            edge = []
            end = n - i
            for k in range(i, end):
                edge.append(matrix[i][k])
            for k in range(i + 1, end):
                edge.append(matrix[k][-i-1])
            for k in range(end - 2, i-1, -1):
                edge.append(matrix[-i-1][k])
            for k in range(end - 2, i, -1):
                edge.append(matrix[k][i])
            l = end - i - 1
            edge = edge[-l:] + edge[:len(edge) - l]
            p = 0
            for k in range(i, end):
                matrix[i][k] = edge[p]
                p += 1
            for k in range(i + 1, end):
                matrix[k][-i-1] = edge[p]
                p += 1
            for k in range(end - 2, i-1, -1):
                matrix[-i-1][k] = edge[p]
                p += 1
            for k in range(end - 2, i, -1):
                matrix[k][i] = edge[p]
                p += 1
        for j in range((n + 1)//2):
            rotate_edge(j)
