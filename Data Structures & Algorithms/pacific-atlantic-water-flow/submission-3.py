class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]
            i, j = node
            res = [False, False]
            if i == 0 or j == 0:
                res[0] = True
            if i == len(heights) - 1 or j == len(heights[0]) - 1:
                res[1] = True
            neighbors = []
            if i > 0:
                neighbors.append((i - 1, j))
            if j > 0:
                neighbors.append((i, j - 1))
            if i < len(heights) - 1:
                neighbors.append((i + 1, j))
            if j < len(heights[0]) - 1:
                neighbors.append((i, j + 1))
            visited[node] = res
            for n in neighbors:
                child_res = [False, False]
                y, x = n
                if heights[y][x] <= heights[i][j]:
                    child_res = dfs((y, x))
                    if child_res[0] and child_res[1]:
                        res[0] = child_res[0]
                        res[1] = child_res[1]
                        return res
                    else:
                        res[0] = res[0] or child_res[0]
                        res[1] = res[1] or child_res[1]
            return res
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                node = (i, j)
                if node not in visited:
                    dfs(node)
                if visited[node][0] and visited[node][1]:
                    res.append([i, j])
        return res
