import sys

sys.setrecursionlimit(10**6)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def helper(start: int):
            if start >= len(nums):
                return False
            for i in range(start, start + nums[start] + 1):
                if i == len(nums) - 1:
                    return True
                if i != start and helper(i):
                    return True
            return False
        return helper(0)