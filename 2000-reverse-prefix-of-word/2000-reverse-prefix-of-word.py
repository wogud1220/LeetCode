class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        result = []
        if ch not in word:
            return word
        num = 0
        for w in word:
            stack.append(w)
            num+=1
            if w == ch:
                while len(stack) != 0:
                    result += stack.pop()
                break

        for z in word[num:]:
            result.append(z)

        return ''.join(result)