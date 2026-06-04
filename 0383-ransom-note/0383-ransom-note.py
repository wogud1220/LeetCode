from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        

        hash_A = defaultdict(int)
        hash_B = defaultdict(int)


        for ch in ransomNote:
            hash_A[ch] += 1

        for ch in magazine:
            hash_B[ch] += 1

        # 매거진의 글자를 뜯어서 랜섬노트 만들수있냐

        for k,v in hash_A.items():
            if ((hash_B[k] - hash_A[k]) >= 0):
                continue
            else:
                return False
        return True

        

        