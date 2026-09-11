from collections import defaultdict

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hash = defaultdict(int)
        
        for ch in words[0]:
            hash[ch] += 1

        for word in words[1:]:
            count = defaultdict(int)
            for ch in word:
                count[ch] += 1

            for ch in hash:
                hash[ch] = min(count[ch], hash[ch])

        answer = []

        for k, v in hash.items():
            for _ in range(v):
                answer.append(k)

        return answer





