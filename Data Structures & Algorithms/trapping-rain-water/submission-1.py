class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        t = 0
        pref_max = [0] * n
        suff_max = [0] * n
        pref_max[0] = height[0]
        suff_max[-1] = height[-1]
        for i in range(1,n):
            pref_max[i] = max(pref_max[i-1], height[i])
        for i in range(n-2, -1, -1):
            suff_max[i] = max(suff_max[i+1], height[i])
        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue
            lh = pref_max[i]
            lr = suff_max[i]
            a = min(lh, lr) - height[i]
            t += max(a, 0)
        return t
            


