class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = {*()}
        def helper(i: int, j: int, pos:int):
            if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0:
                return False
            if (i, j) in visited:
                return False
            if pos == len(word) - 1:
                return board[i][j] == word[pos]
            if board[i][j] != word[pos]:
                return False
            visited.add((i, j))
            neighbors = []
            if i > 0:
                neighbors.append((i - 1, j))
            if i < len(board) - 1:
                neighbors.append((i + 1, j))
            if j > 0:
                neighbors.append((i, j - 1))
            if j < len(board[0]) - 1:
                neighbors.append((i, j + 1))
            for x, y in neighbors:
                if helper(x, y, pos + 1):
                    return True
            visited.remove((i, j))
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i, j, 0):
                    return True
        return False




