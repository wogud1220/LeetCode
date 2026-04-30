from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        d = defaultdict(int)

        for ch in s:
            d[ch] += 1
        for ch in t:
            d[ch] -= 1

        return all(v == 0 for v in d.values())