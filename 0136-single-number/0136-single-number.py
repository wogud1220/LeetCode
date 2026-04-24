from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = defaultdict(int)
        for num in nums:
            hash[num] += 1
        for k,v in hash.items():
            if v == 1:
                return k
