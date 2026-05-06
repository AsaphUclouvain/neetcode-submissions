class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False] * numCourses
        reStack = [False] * numCourses
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        def dfs(node):
            if reStack[node]:
                return True

            if visited[node]:
                return False

            visited[node] = True
            reStack[node] = True
            for cur_node in graph.get(node, []):
                if dfs(cur_node):
                    return True
            reStack[node] = False
            return False
        for u in graph:
            if dfs(u):
                return False
        return True

            
            