"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(node, parent):
            if not node:
                return None
            if node.val in visited:
                return visited[node.val]
            visited[node.val] = Node(node.val, [])
            for cur_node in node.neighbors:
                visited[node.val].neighbors.append(dfs(cur_node, node))
            return visited[node.val]
        # if node:
        #     print(node.neighbors[0].neighbors[1].val)
        return dfs(node, None)

