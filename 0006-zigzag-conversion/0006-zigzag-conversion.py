class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        arr = [""] * numRows # ["", "", ""]
        i = 0
        direction = 1
        for ch in s:
            arr[i] += ch

            if i == 0:
                direction = 1

            elif i == numRows - 1:
                direction = -1

            i += direction

        return "".join(arr)



