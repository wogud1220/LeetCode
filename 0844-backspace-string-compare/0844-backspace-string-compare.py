class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for ch in s:
            if len(stack1) > 0:
                if ch == '#':
                    stack1.pop()
                    continue
                else:
                    stack1.append(ch)
                    continue
            else:
                if ch == '#':
                    continue
                stack1.append(ch)



        for ch in t:
            if len(stack2) > 0:
                if ch == '#':
                    stack2.pop()
                    continue
                else:
                    stack2.append(ch)
                    continue
            else:
                if ch == '#':
                    continue
                stack2.append(ch)

        if stack1 == stack2:
            return True
        else:
            return False