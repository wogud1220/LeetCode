from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash = defaultdict(int)

        for ch in s:
            hash[ch] += 1
        for ch in t:
            hash[ch] -= 1
        
        for k, v in hash.items():
            if hash[k] != 0:
                return str(k)