class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result_a = 0
        result_b = 0
        for exponent, i in enumerate(a[::-1], start = 0,):
            result_a += (2**exponent) * int(i)
        for exponent, i in enumerate(b[::-1], start = 0):
            result_b += (2**exponent) * int(i)

        # 4

        result = bin(result_a + result_b)

        return result[2:]