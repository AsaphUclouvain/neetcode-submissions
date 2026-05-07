class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(i):
            if i in visited:
                return 
            visited.add(i)
            for node in graph.get(i, []):
                dfs(node)
        visited = set()
        graph = defaultdict(list)
        count = 0
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count
