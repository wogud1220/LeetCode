class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        up = 0
        down = 0

        while up < len(s) and down < len(t):
            if s[up] == t[down]:
                up += 1
            down += 1

        return up == len(s)
