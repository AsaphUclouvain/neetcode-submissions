from collections import defaultdict

class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0 for _ in range(26)]
        for c in s:
            arr[ord(c) - ord("a")] += 1
        for c in t:
            arr[ord(c) - ord("a")] -= 1
        return all(v == 0 for v in arr)