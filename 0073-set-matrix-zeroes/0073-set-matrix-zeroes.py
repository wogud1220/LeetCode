class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        arr = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    arr.append((i,j))

        for r, c in arr: # (0,0), (0,3)
            for i in range(col):
                matrix[r][i] = 0


        for r, c in arr: # (0,0), (0,3)
            for i in range(row):
                matrix[i][c] = 0