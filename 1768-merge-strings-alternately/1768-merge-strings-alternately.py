class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        len_1 = len(word1)
        len_2 = len(word2)
        flag_1 = False
        flag_2 = False
        smaller = min(len_1, len_2)
        result = ''
        index = 0
        for i in range(smaller):
            result += word1[i]
            result += word2[i]
            if i+1 == len_1:
                flag_1 = True
                index = i+1
            elif i+1 == len_2:
                flage_2 = True
                index = i+1
            else:
                continue
        
        if flag_1 == True:
            result += word2[index:]
        else:
            result += word1[index:]

        return result
            
