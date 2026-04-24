class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':  # left parantheses
                stack.append(i)


            # right parantheses
            else:
                if len(stack) >= 1:
                    a = stack.pop()
                    if a == '[' and i == ']':
                        continue
                    elif a == '(' and i == ')':
                        continue
                    elif a == '{' and i == '}':
                        continue
                    else:
                        return False
                else:
                    return False

        if len(stack) == 0:
            return True
        else: return False

