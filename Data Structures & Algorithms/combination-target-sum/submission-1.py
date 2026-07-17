class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        presence = set()
        def helper(t, memo):
            if t == 0:
                lst = sorted(memo)
                hsh = str(lst)
                if hsh not in presence:
                    res.append(lst)
                    presence.add(hsh)
                return True
            for n in nums:
                if n > t:
                    continue
                memo.append(n)
                helper(t - n, memo)
                memo.remove(n)
            return False
        helper(target, [])
        return res