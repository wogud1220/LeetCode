from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash = defaultdict(int)
        result = []
        for num in arr:
            hash[num] += 1
        

        for k, v in hash.items():
            result.append(v)
        
        result_len = len(result)

        result_set_len = len(set(result))

        if result_len == result_set_len:
            return True
        else:
            return False