from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = defaultdict(int)
        for ch in s:
            hash[ch] += 1

        for k, v in hash.items():
            if v == 1:
                return s.find(k)
        return -1
        