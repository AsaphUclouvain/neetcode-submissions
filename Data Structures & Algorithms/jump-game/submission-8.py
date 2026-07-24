import sys


sys.setrecursionlimit(10**6)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(cur: int, memo: List[int]):
            if cur in memo:
                return memo[cur]
            if cur == len(nums) - 1:
                memo[cur] = True
                return True
            end = min(len(nums) - 1, cur + nums[cur])
            for i in range(cur + 1, end + 1):
                if dfs(i, memo):
                    memo[cur] = True
                    return True
            memo[cur] = False
            return False
        return dfs(0, {})