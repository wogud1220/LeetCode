from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = defaultdict(int)
        i = 0
        max_len = 0

        for j in range(len(s)):
            if s[j] in hash:
                i = max(i, hash[s[j]] + 1)

            hash[s[j]] = j
            max_len = max(max_len, j - i + 1)

        return max_len