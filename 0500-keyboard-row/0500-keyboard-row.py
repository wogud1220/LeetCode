class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"


        result = []

        for word in words:
            first_val = 0
            second_val = 0
            third_val = 0
            real_word = word
            word = word.lower()

            for ch in word:
                if ch in first_row:
                    first_val = 1
                elif ch in second_row:
                    second_val = 1
                else:
                    third_val = 1
            
            if(first_val + second_val + third_val == 1):
                result.append(real_word)
                print(1)

        return result
            

        