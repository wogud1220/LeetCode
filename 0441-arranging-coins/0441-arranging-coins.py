import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = int((2*n)**0.5)
        while (k+1)*(k+2)//2 <= n:
            k += 1
        while k*(k+1)//2 > n:
            k -= 1
        return k