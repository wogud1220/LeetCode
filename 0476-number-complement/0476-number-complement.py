class Solution:
    def findComplement(self, num: int) -> int:
        # 1. change to num's binary
        binary_num = bin(num)
        binary_num = binary_num[2:]
        # 2. change to complement
        result = ''
        for _ in binary_num:
            if _ == '1':
                result += '0'
            else:
                result += '1'
        # 3. change to dec

        #           str
        real_result = 0
        for i, num in enumerate(result[::-1], start = 0):
            real_result += (2**i) * int(num)
            
        return real_result