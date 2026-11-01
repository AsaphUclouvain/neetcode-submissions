from collections import defaultdict

class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        for c in t:
            d[c] -= 1
        for c in d:
            if d[c] != 0:
                return False
        return True
