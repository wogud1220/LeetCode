from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False


        hash = defaultdict(int)
        hash2 = defaultdict(int)

        for ch, ch2 in zip(s, t):
            hash[ch] += 1
            hash2[ch2] += 1
        
        for k,v in hash.items():
            if hash2[k] != v:
                return False
        return True


