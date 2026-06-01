class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        dp = [[0] * (_) for _ in range(1, rowIndex+2)] # 3
        

        for i in range(rowIndex + 1):
            dp[i][0] = 1

            dp[i][i] = 1

            for i in range(2, rowIndex + 1):
                for j in range(1, i):
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

        return dp[rowIndex]