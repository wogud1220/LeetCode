class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        result = []
        # ["the", "sky", "is", "blue"]
        for _ in s[::-1]:
            result.append(_)
        return ' '.join(result)