class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = nums[0]
        Sum = nums[0]
        for cur in nums[1:]:
            curSum = max(cur, curSum + cur)
            Sum = max(Sum, curSum)
        return Sum