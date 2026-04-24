class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x) # int -> string
        len_x = len(x)
        i = 0
        while i < len_x:
            if x[i] == x[len_x-1-i]:
                i+=1
                continue
            else:
                return False
            

        return True
        