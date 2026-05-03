class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(arr, memo, i):
            if i >= len(arr):
                return 0
            if i in memo:
                return memo[i]
            steal = arr[i] + dp(arr, memo, i + 2)
            skip = dp(arr, memo, i + 1)
            memo[i] = max(steal, skip)            
            return memo[i]
        if len(nums) == 1:
            return nums[0]
        return max(dp(nums[:-1], {}, 0), dp(nums[1:], {}, 0))
