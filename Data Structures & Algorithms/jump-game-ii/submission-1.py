class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i: int, jmp: int) -> None:
            if i in memo:
                memo[i] = min(memo[i], jmp)
                return memo[i]
            else:
                memo[i] = jmp
            end = min(i + nums[i], len(nums) - 1)
            for j in range(end, i, -1):
                dfs(j, jmp + 1)
        dfs(0, 0)
        return memo[len(nums) - 1]
        