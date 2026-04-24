class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        # window slicing
        len_needle = len(needle)

        for i in range(len(haystack)):
            if needle == haystack[i:len_needle+i]:
                return i
        return -1