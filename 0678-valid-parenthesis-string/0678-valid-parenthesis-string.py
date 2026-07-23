class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

        for i, ch in enumerate(s, start = 0):
            if ch == '(':
                left.append(i)

            elif ch == '*':
                star.append(i)

            else:  # ')'
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while left and star:
            if left[-1] > star[-1]:
                return False

            left.pop()
            star.pop()

        return len(left) == 0