from collections import defaultdict

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        hash = defaultdict(int)
        s1 = s1.split()
        s2 = s2.split()
        result = []

        for word in s1:
            hash[word] += 1

        for word in s2:
            hash[word] += 1

        for k, v in hash.items():
            if (v == 1):
                result.append(k)
        return result