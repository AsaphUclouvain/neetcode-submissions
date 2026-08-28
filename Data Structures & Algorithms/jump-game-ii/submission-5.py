class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        l = r = 0
        while r < n - 1:
            farthest = 0
            # print([i for i in range(0,1)])
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res