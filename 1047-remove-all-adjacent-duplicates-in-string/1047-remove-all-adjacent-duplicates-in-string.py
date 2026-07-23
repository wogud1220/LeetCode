class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for ch in s:
            if len(stack) > 0:
                if stack[-1] == ch:
                    stack.pop()
                    continue
                
                else:
                    stack.append(ch)
                    continue

            else:
                stack.append(ch)
                continue
        return ''.join(stack)