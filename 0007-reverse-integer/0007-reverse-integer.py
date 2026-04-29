class Solution:
    def reverse(self, x: int) -> int:
        result =[]
        str_x = str(x)
        


        if x < 0: # minus True
            for i in str_x[:0:-1]:
                result.append(i)
            result = ''.join(result)
            result = '-' + result
            result = int(result)
        else:
            for i in str_x[::-1]:
                result.append(i)

            result = ''.join(result)
            result = int(result)
        

        if result >= (2**31) -1 or result <= -(2**31):
            return 0

            
        return result
        
        
        

        