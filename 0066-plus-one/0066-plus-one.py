class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ''.join(map(str,digits))
        a = int(a) + 1
        a = str(a)
        arr =[]
        for ch in a:
            ch = int(ch)
            arr.append(ch)
        return arr