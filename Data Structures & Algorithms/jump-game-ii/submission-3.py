class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # memo = {}
        # def dfs(i: int, jmp: int) -> None:
        #     if i in memo:
        #         memo[i] = min(memo[i], jmp)
        #         return memo[i]
        #     else:
        #         memo[i] = jmp
        #     end = min(i + nums[i], len(nums) - 1)
        #     for j in range(end, i, -1):
        #         dfs(j, jmp + 1)
        # dfs(0, 0)
        # return memo[len(nums) - 1]
        res = 0
        l = r = 0

        # while r < len(nums) - 1:
        #     farthest = 0
        #     for i in range(l, r+1):
        #         farthest = max(farthest, i + nums[i])
        #     l = r + 1
        #     r = farthest
        #     res += 1
        # return res
