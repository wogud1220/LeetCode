class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        left = 0

        for right in range(len(s)+1):
            if right == len(s) or s[right] == ' ':
                for i in range(right-1, left-1, -1):
                    result += s[i]
                if right != len(s):
                    result += ' '

                left = right + 1

        return result