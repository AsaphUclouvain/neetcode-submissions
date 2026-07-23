import sys
sys.setrecursionlimit(10**6)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def helper(start: int, memo: List[int]):
            if start >= len(nums):
                return False
            if start in memo:
                return memo[start]
            for i in range(start, start + nums[start] + 1):
                if i == len(nums) - 1 or (i != start and helper(i, memo)):
                    memo[start] = True
                    return True
            memo[start] = False
            return False
        return helper(0, {})