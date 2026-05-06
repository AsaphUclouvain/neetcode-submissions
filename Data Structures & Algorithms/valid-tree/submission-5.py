class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        graph = {}
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for cur_node in graph.get(node, []):
                if cur_node == parent:
                    continue
                if not dfs(cur_node, node):
                    return False
            return True
        if len(edges) == 0:
            return True 
        first = 101
        for e in edges:
            if e[0] == e[1]:
                return False
            if e[0] in graph:
                graph[e[0]].append(e[1])
            else:
                graph[e[0]] = [e[1]]
            if e[1] in graph:
                graph[e[1]].append(e[0])
            else:
               graph[e[1]] = [e[0]]
            first = min(first, e[0], e[1])
        print(graph)
        return dfs(first, first) and len(visited) == len(graph)